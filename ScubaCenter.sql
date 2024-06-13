-- create database scubacenter;
-- use scubacenter;

create table if not exists Customer(
CustomerNum char (10) primary key, 
CustomerName varchar(20),
DiverNum char (10),
PassportNum char (9),
Birthdate date,
Gender enum ('male', 'female'),
Email varchar (320),
PhoneNum varchar (15)
);

create table if not exists Certifications (
CertificationLevel varchar (100),
Specialty varchar(100),
primary key(CertificationLevel,Specialty)
);

create table if not exists CustomerCertifications (
CustomerNum char (10),
CertificationLevel varchar (100),
Specialty varchar(100),
primary key(CustomerNum, CertificationLevel,Specialty),
foreign key (CustomerNum) references Customer(CustomerNum),
foreign key (CertificationLevel, Specialty) references Certifications(CertificationLevel,Specialty)
);

create table if not exists Instructor(
InstructorNum char (6) primary key,
InstructorName char(20),
Birthdate date,
Gender enum ('male', 'female'),
Email varchar (320),
PhoneNum varchar (15)
);

create table if not exists DiveAppointment (
BookingNum char (10) primary key,
BookingDate date,
InstructorNum char (10),
CustomerNum char (10),
BookingStatus enum ('pending','canceled','confirmed'),
foreign key (CustomerNum) references Customer(CustomerNum),
foreign key (InstructorNum) references Instructor(InstructorNum)
);

create table if not exists Equipment(
EquipmentNum char (10) primary key,
CustomerNum char(10),
InstructorNum char(10),
EquipmentName varchar (30),
EquipmentSize varchar (15),
DateBorrowed date,
DateReturned date,
foreign key (CustomerNum) references Customer(CustomerNum),
foreign key (InstructorNum) references Instructor(InstructorNum)
);

create table if not exists DiveLog(
BookingNum char (10),
DiveDate date,
DiveDuration int,
DiveDepth int,
DiveType varchar (25),
primary key(BookingNum, DiveDate),
foreign key(BookingNum) references DiveAppointment (BookingNum)

);


create table if not exists DiveLocation( 
DiveLocationName varchar (100),
BookingNum char (10) ,
primary key (DiveLocationName,BookingNum),
foreign key (BookingNum) references DiveAppointment (BookingNum)
);

-- inserts into customer table
insert into customer values ('1908EF6393', 'Youssef', 'D00300009', 'A32000101', '2003-06-18','male', 'youssefg03@gmail.com', '01011149023');
insert into customer values ('C00007349', 'Ali', 'D00300007', 'A23211010', '2003-09-30','male', 'ali@gmail.com', '01093249023');
insert into customer values ('1918FF6374', 'Fadi', 'D00300003', 'A21200012', '2003-10-03','male', 'fadi@gmail.com', '01111119023');
insert into customer values ('C00007338', 'Ilham', 'D00300002', 'A21288192', '2003-11-23','female', 'ilham@gmail.com', '01937519023');

-- inserts into instructor table
insert into Instructor values ('637147', 'Nour', '2003-01-18','female', 'nour@gmail.com', '01011149023');
insert into Instructor values ('638347', 'Mariam', '2003-04-30','female', 'mariam@gmail.com', '01093249023');
insert into Instructor values ('637000', 'Nadine', '2003-12-03','female', 'nad@gmail.com', '01111119023');
insert into Instructor values ('557532', 'Omar', '2003-11-02','male', 'omar@gmail.com', '01937519023');

-- inserts into certifications table
insert into Certifications values ('Open Water','Altitude Diver');
insert into Certifications values ('Open Water','AWARE Shark');
insert into Certifications values ('Open Water','Enriched Air Diver');
insert into Certifications values ('Advanced Open Water','Cavern Diver');
insert into Certifications values ('Advanced Open Water','Ice Diver');
insert into Certifications values ('Advanced Open Water','Wreck Diver');

-- inserts into customer certifications
insert into CustomerCertifications values ('1908EF6393','Open Water','Altitude Diver');
insert into CustomerCertifications values ('1908EF6393','Open Water','AWARE Shark');
insert into CustomerCertifications values ('C00007338','Open Water','Enriched Air Diver');
insert into CustomerCertifications values ('1918FF6374','Advanced Open Water','Cavern Diver');
insert into CustomerCertifications values ('1918FF6374','Advanced Open Water','Ice Diver');
insert into CustomerCertifications values ('1918FF6374','Advanced Open Water','Wreck Diver');

-- inserts into DiveAppointment
insert into DiveAppointment values ('D00300009','2024-05-18','637147','1908EF6393','Confirmed');
insert into DiveAppointment values ('D00300008','2024-05-18',637147,'1908EF6393','Pending');
insert into DiveAppointment values ('D00300007','2024-05-20','557532','1908EF6393','Canceled');
insert into DiveAppointment values ('D00300006','2024-06-7','637000','1908EF6393','Pending');
insert into DiveAppointment values ('D00300005','2024-06-18','557532','1908EF6393','Confirmed');
insert into DiveAppointment values ('D00300004','2024-06-27','637147','1908EF6393','Confirmed');

-- Dive Location 
insert into DiveLocation values ('House Reef','D00300009');
insert into DiveLocation values ('Sharks Point','D00300008');
insert into DiveLocation values ('House Reef','D00300007');
insert into DiveLocation values ('House Reef','D00300006');
insert into DiveLocation values ('Chasm Reef','D00300005');
insert into DiveLocation values ('Chasm Reef','D00300004');

-- Dive Log
insert into DiveLog values ('D00300009','2024-05-18',60,17,'Regular');
insert into DiveLog values ('D00300008','2024-05-18',40,24,'Boat');
insert into DiveLog values ('D00300007','2024-05-20',35,28,'Regular');
insert into DiveLog values ('D00300006','2024-06-7',45,22,'Regular');
insert into DiveLog values ('D00300005','2024-06-18',32, 29,'Boat');
insert into DiveLog values ('D00300004','2024-06-27',30, 32,'Boat');

-- Queries
-- output divelog


select d.bookingnum, d.instructorNum, dl.divedepth ,dl.diveduration,dl.divedate, dloc.divelocationname
from diveappointment d 
inner join customer c 
on d.customernum = c.customernum
inner join divelog dl
on d.bookingnum = dl.bookingnum
inner join divelocation dloc
on d.bookingnum = dloc.bookingnum
where d.customernum = '1908EF6393';



select c.customername , d.customernum, d.bookingnum, d.instructorNum, dl.divelocationname, d.bookingdate
from diveappointment d
inner join customer c on d.customernum = c.customernum
inner join divelocation dl on d.bookingnum = dl.bookingnum;



select max(divedepth) as 'Max Depth' from divelog;

SELECT c.CustomerName, c.CustomerNum, dl.DiveDepth
FROM Customer c
JOIN DiveAppointment da ON c.CustomerNum = da.CustomerNum
JOIN DiveLog dl ON da.BookingNum = dl.BookingNum
ORDER BY dl.DiveDepth ASC
LIMIT 1;


