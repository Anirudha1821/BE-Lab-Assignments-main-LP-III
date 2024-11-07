pragma solidity ^0.8.0;

contract StudentContract{
    struct Student{
        uint rollno;
        string name;
    }
    Student[] studentData;

    function addStudent(uint rollno,string memory name) public{
        studentData.push(Student(rollno,name));
    }
    receive() external payable { }

    function getStudent(uint rollno) public view returns (Student memory){
        for(uint i=0;i<studentData.length;i++){
            if(studentData[i].rollno==rollno){
                return studentData[i];
            }
        }
        revert("Student does not exist");
    }

    fallback() external payable{}
}