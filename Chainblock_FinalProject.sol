pragma solidity ^0.8.7;

import "@openzeppelin/contracts/utils/Strings.sol";

contract Library {

    struct Book {
        uint id;            //book id
        string name;        //book name
        string author;      //book author
        string publisher;   //book publisher
        bool state;         //book state 1:can borrowed, 0: being borrowed
        uint time;          //when someone borrowed it will have time
    }

    struct Person {
        uint user_id;       //user id
        string name;        //user name
        address addr;       //address
        bool state;         //user credit 1:good, 0:bad
    }

    Book [] public collection;      //existing collection
    Person [] public member;        //existing member
    uint public memberNum;
    uint public collectionNum;

    //when this library created, add 10 books as default collection
    constructor() public {          
        memberNum = 0;
        collectionNum = 0;
        collection.push(Book({id: collectionNum++, name: "Object-oriented programming",author: "Mr.Wang",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "Chances and Statistics",author: "Mr.Wang",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "Operating System",author: "Mr.Lee",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "Computer Architecture",author: "Mr.Lee",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "Electronic Devices",author: "Mr.Chen",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "Linear Algebra",author: "Mr.Chen",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "Information Security",author: "Mr.Su",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "Network intrusion detection",author: "Mr.Su",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "Chain Block",author: "Mr.Wang",publisher: "MCU",state: true,time: 0}));
        collection.push(Book({id: collectionNum++, name: "IoT",author: "Mr.Wang",publisher: "MCU",state: true,time: 0}));
    }

    //key in name, author, publisher can add a book in collection, and will auto give an ID and set state and time
    function AddBook(string memory name, string memory author, string memory publisher) public {
        collection.push(Book({
            id: collectionNum++,
            name: name,
            author: author,
            publisher: publisher,
            state: true,
            time: 0
        }));
    }
    
    //key in name, library will auto give him/her/??? an ID and credit state
    function AddMember(string memory name) public {
        member.push(Person({
            user_id: memberNum++,
            name: name,
            addr: msg.sender,
            state: true
        }));
    }

    //It's have to be a Member to borrow a book 
    //key in name and exist book and the time you want to borrowed(no limited)
    function BorrowBook(string memory person, string memory book, uint time) public {
        for(uint i=0; i<member.length; i++){
                if(keccak256(abi.encodePacked(member[i].name)) == keccak256(abi.encodePacked(person))){
                    if(member[i].state != false){
                    for(uint j=0; j<collection.length; j++){
                        if(keccak256(abi.encodePacked(collection[j].name)) == keccak256(abi.encodePacked(book))){
                            collection[j].state = false;
                            collection[j].time = block.timestamp + time;
                        }
                    }
                }
            }
        }
    }


    //It's have to be a Member to escheat a book 
    //key in name and exist book and it will detected you escheat it on time or not
    //if you're late, then your ban from this libray lmao
    function EscheatBook(string memory person, string memory book) public {
        for(uint i=0; i<collection.length; i++){
            if(keccak256(abi.encodePacked(collection[i].name)) == keccak256(abi.encodePacked(book))){
                if(block.timestamp > collection[i].time){
                    for(uint j=0; j<member.length; j++){
                        if(keccak256(abi.encodePacked(member[j].name)) == keccak256(abi.encodePacked(person))){
                            member[j].state = false;
                        }
                    }
                }
                collection[i].time = 0;
                collection[i].state = true;
            }
        }
    }

    //get every books in collection
    function getBookList() public view returns (Book [] memory){
        return collection;
    }

    //get every members in member
    function getMemberList() public view returns (Person [] memory){
        return member;
    }

    //get member amount
    function getMemberAmount() public view returns (uint){
        return memberNum;
    }

    //get book amount
    function getBookAmount() public view returns (uint){
        return collectionNum;
    }

    //key in book name you can search the book and check it's been borrowed or not
    function checkBookStates(string memory name) public view returns (bool){
        for(uint i=0; i<collection.length; i++){
            if(keccak256(abi.encodePacked(collection[i].name)) == keccak256(abi.encodePacked(name))){
                return collection[i].state;
            }
        }
    }

    //just a function to check this person is a member or not
    function checkPersonIsMember(string memory name) public view returns (bool){
        for(uint i=0; i<member.length; i++){
            if(keccak256(abi.encodePacked(member[i].name)) == keccak256(abi.encodePacked(name))){
                return true;
            }
        }
        return false;
    }
    function append(string memory a, string memory b) internal pure returns (string memory) {
        return string(abi.encodePacked(a, b));
    }

    function bigappend(string  memory a, string  memory b, string memory  c, string  memory d, string  memory e) internal pure returns (string memory) {
        return string(abi.encodePacked(a, b, c, d, e));
    }
}