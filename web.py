import json
from web3 import Web3
import remi.gui as gui
from remi import start, App


class MyWeb(App):

    ganache_url = "http://127.0.0.1:8545"

    web3 = Web3(Web3.HTTPProvider(ganache_url))

    web3.eth.defaultAccount = web3.eth.accounts[0]

    abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"author","type":"string"},{"internalType":"string","name":"publisher","type":"string"}],"name":"AddBook","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"AddMember","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"person","type":"string"},{"internalType":"string","name":"book","type":"string"},{"internalType":"uint256","name":"time","type":"uint256"}],"name":"BorrowBook","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"person","type":"string"},{"internalType":"string","name":"book","type":"string"}],"name":"EscheatBook","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"checkBookStates","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"checkPersonIsMember","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"collection","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"author","type":"string"},{"internalType":"string","name":"publisher","type":"string"},{"internalType":"bool","name":"state","type":"bool"},{"internalType":"uint256","name":"time","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"collectionNum","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBookAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBookList","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"author","type":"string"},{"internalType":"string","name":"publisher","type":"string"},{"internalType":"bool","name":"state","type":"bool"},{"internalType":"uint256","name":"time","type":"uint256"}],"internalType":"struct Library.Book[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMemberAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMemberList","outputs":[{"components":[{"internalType":"uint256","name":"user_id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"addr","type":"address"},{"internalType":"bool","name":"state","type":"bool"}],"internalType":"struct Library.Person[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"member","outputs":[{"internalType":"uint256","name":"user_id","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"addr","type":"address"},{"internalType":"bool","name":"state","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"memberNum","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

    address = web3.toChecksumAddress(
        "0xE1d33710D21aC99176E846A3a4D305871Cc68A44")

    contract = web3.eth.contract(address=address, abi=abi)

    def __init__(self, *args):
        super(MyWeb, self).__init__(*args)

    def main(self):

        verticalContainer = gui.Container(width=1000, margin='0px auto', style={
                                            'display': 'block', 'overflow': 'hidden'})

        horizontalContainer = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_HORIZONTAL, margin='0px', style={
                                            'display': 'block', 'overflow': 'auto'})

        subContainerLeft = gui.Container(
            width=700, style={'display': 'block', 'overflow': 'auto', 'text-align': 'center'})

        subContainerRight = gui.Container(
            width=300, style={'display': 'block', 'overflow': 'auto', 'text-align': 'center'})

        self.table = gui.Table.new_from_list([
            ('ID', 'Book name', 'Author', 'Publisher', 'State', 'Time')],
            width=680, height='95%', margin='10px')

        self.resultLbl = gui.Label(width=280, height=30, margin='10px')

        '''--------------------------------------'''
        self.addMemTxt = gui.TextInput(width=280, height=30, margin='10px')
        self.addMemTxt.set_text('Add Member')

        self.addMemBtn = gui.Button(
            'Add Member', width=280, height=30, margin='10px')
        self.addMemBtn.onclick.do(self.addMem)

        '''--------------------------------------'''
        self.addBookNameTxt = gui.TextInput(
            width=280, height=30, margin='10px')
        self.addBookNameTxt.set_text('Book name')
        self.addBookAuthorTxt = gui.TextInput(
            width=280, height=30, margin='10px')
        self.addBookAuthorTxt.set_text('Author')
        self.addBookPublisherTxt = gui.TextInput(
            width=280, height=30, margin='10px')
        self.addBookPublisherTxt.set_text('Publisher')

        self.addBookBtn = gui.Button(
            'Add Book', width=280, height=30, margin='10px')
        self.addBookBtn.onclick.do(self.addBook)

        '''--------------------------------------'''
        self.borrowerTxt = gui.TextInput(width=280, height=30, margin='10px')
        self.borrowerTxt.set_text('Name')
        self.borrowBookTxt = gui.TextInput(width=280, height=30, margin='10px')
        self.borrowBookTxt.set_text('Book')
        self.borrowTimeTxt = gui.TextInput(width=280, height=30, margin='10px')
        self.borrowTimeTxt.set_text('Time')

        self.borrowBookBtn = gui.Button(
            'Borrow Book', width=280, height=30, margin='10px')
        self.borrowBookBtn.onclick.do(self.borrow)

        '''--------------------------------------'''
        self.escheaterTxt = gui.TextInput(width=280, height=30, margin='10px')
        self.escheaterTxt.set_text('Name')
        self.escheatBookTxt = gui.TextInput(
            width=280, height=30, margin='10px')
        self.escheatBookTxt.set_text('Book')

        self.escheatBookBtn = gui.Button(
            'Escheat Book', width=280, height=30, margin='10px')
        self.escheatBookBtn.onclick.do(self.escheat)

        '''--------------------------------------'''
        self.checkBookStateTxt = gui.TextInput(
            width=280, height=30, margin='10px')
        self.checkBookStateTxt.set_text('Search Book State')

        self.checkBookStateBtn = gui.Button(
            'Search', width=280, height=30, margin='10px')
        self.checkBookStateBtn.onclick.do(self.checkBookState)

        '''--------------------------------------'''
        self.getBookListBtn = gui.Button(
            'All Book List', width=280, height=30, margin='10px')
        self.getBookListBtn.onclick.do(self.bookList)

        '''--------------------------------------'''
        self.getMemberNumBtn = gui.Button(
            'Member amount', width=280, height=30, margin='10px')
        self.getMemberNumBtn.onclick.do(self.memAmount)

        '''--------------------------------------'''
        self.getBookNumBtn = gui.Button(
            'Book amount', width=280, height=30, margin='10px')
        self.getBookNumBtn.onclick.do(self.bookAmount)

        '''--------------------------------------'''
        subContainerRight.append([
            self.addMemTxt,
            self.addMemBtn,
            self.addBookNameTxt,
            self.addBookAuthorTxt,
            self.addBookPublisherTxt,
            self.addBookBtn,
            self.borrowerTxt,
            self.borrowBookTxt,
            self.borrowTimeTxt,
            self.borrowBookBtn,
            self.escheaterTxt,
            self.escheatBookTxt,
            self.escheatBookBtn,
            self.checkBookStateTxt,
            self.checkBookStateBtn,
            self.getBookListBtn,
            self.getMemberNumBtn,
            self.getBookNumBtn
        ])

        subContainerLeft.append([self.table, self.resultLbl])

        horizontalContainer.append([subContainerLeft, subContainerRight])

        menu = gui.Menu(width='100%', height='50px')

        menubar = gui.MenuBar(width='100%', height='50px')
        menubar.append(menu)

        verticalContainer.append([menubar, horizontalContainer])

        return verticalContainer

    def addMem(self, widget):
        mbname = self.addMemTxt.get_value()
        self.contract.functions.AddMember(mbname).transact()
        self.resultLbl.set_text("Welcome "+mbname+"!")

    def memAmount(self, widget):
        mbnumber = self.contract.functions.getMemberAmount().call()
        self.resultLbl.set_text("Member Amount : "+str(mbnumber))

    def bookAmount(self, widget):
        bnumber = self.contract.functions.getBookAmount().call()
        self.resultLbl.set_text("Book Amount : "+str(bnumber))

    def addBook(self, widget):
        addbookname = self.addBookNameTxt.get_value()
        addbookauthor = self.addBookAuthorTxt.get_value()
        addbookpublisher = self.addBookPublisherTxt.get_value()
        self.contract.functions.AddBook(
            addbookname, addbookauthor, addbookpublisher).transact()
        self.resultLbl.set_text("Add successful.")

    def borrow(self, widget):
        borrowbookname = self.borrowBookTxt.get_value()
        borrower = self.borrowerTxt.get_value()
        borrowtime = self.borrowTimeTxt.get_value()
        isMem = self.contract.functions.checkPersonIsMember(borrower).call()
        if isMem is True :
            self.contract.functions.BorrowBook(
            borrower, borrowbookname, int(borrowtime)).transact()
            self.resultLbl.set_text("Borrow successful.")
        elif isMem is False :
            self.resultLbl.set_text("Your not a member.")
        

    def escheat(self, widget):
        escheatbookname = self.escheatBookTxt.get_value()
        escheater = self.escheaterTxt.get_value()
        isMem = self.contract.functions.checkPersonIsMember(escheater).call()
        if isMem is True :
            self.contract.functions.EscheatBook(
            escheater, escheatbookname).transact()
            self.resultLbl.set_text("Escheat successful.")
        elif isMem is False :
            self.resultLbl.set_text("Your not a member.")
        

    def checkBookState(self, widget):
        bookstate = self.checkBookStateTxt.get_value()
        state = self.contract.functions.checkBookStates(bookstate).call()
        self.resultLbl.set_text("Book State : "+str(state))

    def bookList(self, widget):
        booklist = self.contract.functions.getBookList().call()
        strbooklist = [
            ['ID', 'Book name', 'Author', 'Publisher', 'State', 'Time']]
        for i in range(len(booklist)):
            strbooklist.append(list(map(str, booklist[i])))
        self.table.append_from_list(strbooklist, True)


if __name__ == "__main__":
    # starts the webserver
    start(MyWeb, debug=True, address='127.0.0.1', port=9487,
            start_browser=True, multiple_instance=True)
