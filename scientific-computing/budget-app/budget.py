class Category:
    ledger=""
    balance=""
    name=""
    def __init__(self, name):
        self.name=name
        self.balance=0
        self.ledger=list()

    def deposit(self, amount, description=""):
        self.balance+=amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if(self.check_funds(amount)):
            self.balance-=amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, destiny):
        if(self.withdraw(amount, "Transfer to "+destiny.name)):
            destiny.deposit(amount, "Transfer from "+self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.balance>=amount

    def __str__(self):
        string=""
        title=""
        halfname=len(self.name)//2
        for n in range(15-halfname):
            title+="*"
        title+=self.name
        for n in range(30-len(title)):
            title+="*"
        string+=title+"\n"
        for b in self.ledger:
            if(len(b["description"])<=23):
                string+=b["description"]
                for n in range(23-len(b["description"])):
                    string+=" "
            else:
                for n in range(23):
                  string+=b["description"][n]
            stringamount=str(format(b["amount"],".2f"))
            for n in range(7-len(stringamount)):
                    string+=" "
            string+=stringamount
            string+="\n"
        string+="Total: "+str(format(self.balance,".2f"))
        return string
        


def create_spend_chart(categories):
    string="Percentage spent by category\n"
    linelen=5+(3*len(categories))
    totalwithdraw=0
    withdraws={}
    for c in categories:
        withdraws[c.name]=0
        for l in c.ledger:
            amount=l["amount"]
            if(amount<0):
                withdraws[c.name]-=amount
                totalwithdraw-=amount
    for w in withdraws:
        withdraws[w]/=totalwithdraw
        withdraws[w]*=100
        withdraws[w]//=10
        withdraws[w]*=10
    for p in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]:
        for n in range(3-len(str(p))):
            string+=" "  
        string+=str(p)+"|"
        for w in withdraws:
            string+=" "
            if(withdraws[w]>=p): string+="o"
            else: string+=" "
            string+=" "
        string+=" \n"
    string+="    "
    for n in range(linelen-4):
        string+="-"
    #string+="\n"
    stillname=True
    count=0
    while(stillname):
        newstring="\n    "
        for w in withdraws:
            newstring+=" "
            if(len(w)>count): newstring+=w[count]
            else: newstring+=" "
            newstring+=" "
        newstring+=" "
        count+=1
        if(newstring.isspace()):
            stillname=False
        else:
            string+=newstring



    return string