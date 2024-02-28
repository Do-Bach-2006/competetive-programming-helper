import os 


def get_challange_name() -> str:
    # default name will be new_challange
    name = "new_challange"
    exist_files = set(os.listdir())

    while True:

        print("please enter the new name to create: ")
        name = input().strip()

        if name not in exist_files:
            break

        print("folder exist!")


    return name

def create_directory_and_cd(name: str)-> None:
    os.mkdir(name)
    os.chdir(name)

def create_needed_files(name: str)->None:

    CPP_CONTENT = f"""
#include <iostream>
using namespace std;

int main()
{{
    freopen("{name}.INP" , "r" , stdin);
    freopen("{name}.OUT" , "w" , stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

}}
    """

    PY_CONTENT = f"""
import sys

sys.stdin = open("{name}.INP" , "r")
sys.stdout = open("{name}.OUT", "w")


    """
    



    # create input file
    inp = open(name + ".INP" , "w")
    inp.close()

    # create output file
    out = open(name + ".OUT" , "w")
    out.close()

    # create cpp file and content to it
    cpp = open(name + ".cpp", "w")
    cpp.write(CPP_CONTENT)
    cpp.close()

    # create py file and write content to it
    py = open(name + ".py", "w")
    py.write(PY_CONTENT)
    py.close()


if __name__ == "__main__":
    name = get_challange_name()
    create_directory_and_cd(name)
    create_needed_files(name)


