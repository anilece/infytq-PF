#PF-Exer-23
def translate(bilingual_dict,english_words_list):
  
    swedish_words_list=[""]*len(english_words_list)
    
    bilingual_dict_keys=bilingual_dict.keys()
    for j in range(len(english_words_list)):
        for key,value in bilingual_dict.items():
            
            if key==english_words_list[j]:
                swedish_words_list[j]=bilingual_dict[key]
        
    return swedish_words_list


bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)
