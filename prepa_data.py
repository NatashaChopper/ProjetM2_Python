import csv, sys, os, re
train = sys.argv[1]

def sets_creation():
    with open(train, "r", encoding ="ISO-8859-1") as csv_file:
        with open ("tmp_set_test.txt", "w", encoding = "utf-8") as tmp_test:
            with open("tmp_set_train.txt", "w", encoding="utf-8") as tmp_train:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                test_set = 0
                train_set = 0
                for row in csv_reader:
                    line_count += 1
                    if line_count%3==0:
                        test_set += 1
                        tmp_test.write(str(row))
                        tmp_test.write("\n") 
                    else:
                        train_set += 1
                        tmp_train.write(str(row))
                        tmp_train.write("\n")

                print(f'Processed {train_set} lines for train set.')
                print(f'Processed {test_set} lines for test set.')
sets_creation()

def nettoyage(fic_sale, fic_propre):
    with open(fic_sale, "r", encoding = "UTF-8") as fic_s:
        
        with open(fic_propre, "w", encoding="UTF-8") as fic_p:
            fic_s = fic_s.read().split("\n")
            for i in fic_s:
                i = re.sub(r"\[", "", i)
                i = re.sub(r"\]", "", i)
                fic_p.write(str(i)+"\n")
    os.remove(fic_sale)
nettoyage("tmp_set_test.txt", "test_set.txt")
print("test set is ready")
nettoyage("tmp_set_train.txt", "train_set_all.txt")
print("train set is ready")