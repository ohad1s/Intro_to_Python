def build_mat(n):
    mat=[]
    for i in range(n):
        line=[]
        for j in range(n):
            line.append("")
        mat.append(line)
    return mat


def build_num_sq(n):
    mat=build_mat(n)
    num_to_add=0
    print(mat)
    for i in range(n):
        mat[0][i]=(num_to_add%10)
        num_to_add+=1
    print(mat)
    for i in range(1,n-1):
        mat[i][-1]=(num_to_add%10)
        num_to_add+=1
    print(mat)
    for i in reversed(range(0,n)):
        mat[-1][i]=(num_to_add%10)
        num_to_add += 1
    print(mat)
    for i in reversed(range(1,n-1)):
        mat[i][0]=(num_to_add%10)
        num_to_add += 1
    print(mat)
    return mat

# build_num_sq(5)


class robot:
    def __init__(self,num):
        self.number= num

    def __repr__(self):
        return "robot"

    def fight(self,other):
        if self.number>other.number:
            other.number-=1
        else:
            self.number-=1


class Irobot(robot):

    def __init__(self):
        super().__init__(10)
        self.number2=2


    def __repr__(self):
        return "Irobot"



# r=robot(5)
# print(r)
# ir=Irobot()
# print(ir)


def forward_str(string,n):
    abc="abcdefghijklmnopqrstuvwxyz"
    new_s=""
    for char in string:
        ind=abc.index(char)
        new_ind=ind+n
        enter=new_ind%26
        new_s+=abc[enter]
    return new_s

# print(forward_str("abcxyz",2))

def merge_files(filename1,filename2,outputfile):
    f1=open(filename1,"r")
    f2=open(filename2,"r")
    f1_words=f1.readlines()
    f2_words=f2.readlines()
    f1.close()
    f2.close()
    with open(outputfile,"w") as o_f:
        index_f1=0
        index_f2=0
        while index_f1<len(f1_words) and index_f2<len(f2_words):
            word1=f1_words[index_f1]
            word2=f2_words[index_f2]
            if word1<word2:
                o_f.write(word1)
                o_f.write("\n")
                index_f1+=1
            else:
                o_f.write(word2)
                o_f.write("\n")
                index_f2+=1

        while index_f1<len(f1_words):
            o_f.write(word1)
            o_f.write("\n")
            index_f1 += 1

        while index_f2<len(f2_words):
            o_f.write(word2)
            o_f.write("\n")
            index_f2 += 1


# lst1=[9,2,6,8,3,6,2]
# lst1.sort()
# print(lst1)

# lst2=[9,2,6,8,3,6,2]
# sorted_list=sorted(lst2,key=lambda x:x.getRight()+x.getLeft(),reverse=True)
# print(lst2)
# print(sorted_list)




