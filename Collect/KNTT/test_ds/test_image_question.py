import json
import os 

if __name__ == '__main__':
    kn10_file = os.path.dirname(os.path.abspath(__file__)) + '/../KNTT-10.json'
    with open(kn10_file ,'r', encoding='utf-8') as f:
        kn10_questions = json.load(f)
    print('KNTT 10 questions: ', len(kn10_questions))
    kn10_img_question_count = 0
    for q in kn10_questions:
        text_check = q['Context'] + q['Question'] + q['Options']
        if any(s in text_check for s in ["http://", "https://", "<img", "<svg"]):
            kn10_img_question_count +=1
    print('KNTT 10 questions(contain image): ', kn10_img_question_count)

    kn11_file = os.path.dirname(os.path.abspath(__file__)) + '/../KNTT-11.json'
    with open(kn11_file ,'r', encoding='utf-8') as f:
        kn11_questions  = json.load(f)
    print('KNTT 11 questions: ', len(kn11_questions))
    kn11_img_question_count = 0
    for q in kn11_questions:
        text_check = q['Context'] + q['Question'] + q['Options']
        if any(s in text_check for s in ["http://", "https://", "<img", "<svg"]):
            kn11_img_question_count +=1
    print('KNTT 11 questions(contain image): ', kn11_img_question_count)

    kn12_file = os.path.dirname(os.path.abspath(__file__)) + '/../KNTT-12.json'
    with open(kn12_file ,'r', encoding='utf-8') as f:
        kn12_questions  = json.load(f)
    print('KNTT 12 questions: ', len(kn12_questions))
    kn12_img_question_count = 0
    for q in kn12_questions:
        text_check = q['Context'] + q['Question'] + q['Options']
        if any(s in text_check for s in ["http://", "https://", "<img", "<svg"]):
            kn12_img_question_count +=1
    print('KNTT 12 questions(contain image): ', kn12_img_question_count)
