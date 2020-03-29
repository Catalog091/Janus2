import pandas as pd
import re
from uuid import uuid4
import emoji
import en_core_web_sm
from Janus.rule_sets import rule_sets
from spacy.matcher import PhraseMatcher


pd.set_option('display.max_columns', None)


class Janus(object):

    def __init__(self):
        self.threat_level = 0
        self.nlp = en_core_web_sm.load()

    def target_search(self, inputs):

        parse_dict = {}
        uid = uuid4()

        def string_preprocess(d_text):

            emails = ['gmail', 'hotmail', 'outlook', 'yahoo', 'aol', 'icloud', 'mail', 'gmx', 'protonmail',
                      'tutanota', 'mac']
            emails_patterns = '(' + '|'.join(emails) + ')'

            to_remove = "_.-"
            pattern = "(?P<char>[" + re.escape(to_remove) + "])(?P=char)+"
            _RE_COMBINE_WHITESPACE = re.compile(r"\s+")

            t = re.sub('[!#,:_()\-<>/?\‿\◢\◣\▃\]\[]', '', d_text.lower())
            at = _RE_COMBINE_WHITESPACE.sub(' ', t).strip()
            bt = re.sub(emoji.get_emoji_regexp(), r"", at)
            ct = re.sub(pattern, r"\1", bt)

            res = any(ele in ct for ele in emails)

            if res:
                match_emails = filter(lambda x: x in ct, emails)
                for name in match_emails:
                    if "@" + name + '.' not in ct:
                        dt = re.sub(emails_patterns, r'@\1.', ct)
                        self.threat_level += 0.9
                        return dt
                    else:
                        return ct
            else:
                return ct

        def detect_phone_numbers(p_text):

            redirects = ['whatsapp', 'jabber', 'telegram', 'wicker', 'signal']

            res = any(ele in p_text for ele in redirects)

            if res:
                self.threat_level += 0.9

            phone_dict = {}

            area_df = pd.read_csv('/Users/workitywork/PycharmProjects/Curation/Janus/area_codes.csv').reset_index()
            area_codes = dict(zip(area_df.state, area_df.codes))

            phone_regex = re.compile(r"(\+420)?\s*?(\d{3})\s*?(\d{3})\s*?(\d{4})")
            groups = phone_regex.findall(p_text)
            for g in groups:
                number = "".join(g)
                if number is None:
                    pass
                else:
                    area = str(number)[:2]
                    for state, codes in area_codes.items():
                        if area in codes:
                            phone_dict['Phone_Number'] = [number, state]
                            return phone_dict

        def detect_email(parse_text):

            email_dict = {}
            email = re.findall('\S+@\S+', parse_text)
            if len(email) == 0:
                pass
            else:
                email_dict['Email_Address'] = email
                return email_dict

        def entity_finder(parse_text):

            doc = self.nlp(parse_text)
            junk_terms = []
            entity_dict = {}
            chunk = [(X.text, X.label_) for X in doc.ents]

            location_list = set()
            nat_rel_list = set()
            geo_pol_list = set()

            for i in chunk:

                if i[1] == 'LOC' and i[0] not in junk_terms:
                    location_list.add(('Location: ', i[0]))
                elif i[1] == 'NORP' and i[0] not in junk_terms:
                    nat_rel_list.add(('Nationalities or religious or political groups: \n', i[0]))
                elif i[1] == 'GPE' and i[0] not in junk_terms:
                    geo_pol_list.add(('Countries, cities, states: \n', i[0]))

            master_list = [location_list, nat_rel_list, geo_pol_list]
            if len(master_list) <= 3:
                pass
            else:
                entity_dict['Extracted_Entities'] = master_list
                return entity_dict

        def phrase_threat_finder(t_text):

            phrase_matcher = PhraseMatcher(self.nlp.vocab)

            rules = rule_sets()
            flag_dict = {}
            triggered = []

            for trigger, terms in rules.items():

                patterns = [self.nlp(text) for text in terms]
                phrase_matcher.add(trigger, None, *patterns)
                sentence = self.nlp(t_text)

                matched_phrases = phrase_matcher(sentence)

                for match_id, start, end in matched_phrases:
                    string_id = self.nlp.vocab.strings[match_id]
                    span = sentence[start:end]
                    indicators = str(string_id) + ": " + str(span.text)
                    triggered.append(indicators)

            final_triggers = list(set(triggered))

            if len(final_triggers) == 1:
                self.threat_level += 0.17

            elif len(final_triggers) == 2:
                self.threat_level += 0.34

            elif len(final_triggers) == 3:
                self.threat_level += 0.51

            elif len(final_triggers) == 4:
                self.threat_level += 0.68

            elif len(final_triggers) == 5:
                self.threat_level += 0.85

            elif len(final_triggers) == 6:
                self.threat_level += 1

            test_l = final_triggers

            if len(test_l) == 0:
                pass
            else:
                flag_dict['Alert_Phrases'] = final_triggers
                return flag_dict

        text = string_preprocess(inputs)

        def final_score(score_list):

            score = 100 * score_list / 9

            if score == 0.0:
                pass
            elif score >= 90:
                return score, "Very Critical"
            elif 80 <= score < 90:
                return score, "Critical"
            elif 65 <= score < 80:
                return score, "High"
            elif 25 <= score < 65:
                return score, "Medium"
            elif 0 <= score < 25:
                return score, "Low"

        parse_dict[uid] = [detect_email(text),
                           detect_phone_numbers(text),
                           entity_finder(text),
                           final_score(self.threat_level),
                           phrase_threat_finder(text)]

        for tid, vals in parse_dict.items():
            if all(v is None for v in vals):
                return 0
            else:
                return parse_dict


reach = Janus()



test_data = pd.read_csv('/Users/workitywork/PycharmProjects/Curation/Janus/Final_test_scoring_RF.csv')
test_list = test_data.title.tolist()

test = []

for i, j in enumerate(test_list):
    res = [reach.target_search(j)]
    if res and all(elem == 0 for elem in res):
        pass
    else:
        test.append(res)

out_put = pd.DataFrame(test)
out_put.to_csv('/Users/workitywork/PycharmProjects/Curation/Janus/Final_test_scoring_RF.csv')

if __name__=="__main__":
    Janus()



