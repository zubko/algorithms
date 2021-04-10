-- 175. Combine Two Tables
-- Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people

-- Schema

create table Person (PersonId int, FirstName varchar(255), LastName varchar(255));
create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255));
truncate table Person;
insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen');
insert into Person values(2, "Ada", "Coe");
insert into Person values(3, "Jessy", "James");
truncate table Address;
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York');
insert into Address values(1, 1, "New York", "NY");
insert into Address values(3, 1, "San Francisco", "CA");
insert into Address values(2, 3, "Boston", "MS");

-- Solution

select Person.FirstName, Person.LastName, Address.City, Address.State
from Person
left join Address on Person.PersonId = Address.PersonId;

