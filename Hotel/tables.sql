drop database if exists hotel;

create database hotel;

use hotel;

DROP TABLE IF EXISTS Reservations;
DROP TABLE IF EXISTS Guests;
DROP TABLE IF EXISTS Addresses;
DROP TABLE IF EXISTS Room;
DROP TABLE IF EXISTS RoomType;
DROP TABLE IF EXISTS Amenities;
DROP TABLE IF EXISTS Room_Amenities;


-- create
CREATE TABLE Addresses (
  ID INTEGER PRIMARY KEY,
  Address VARCHAR(200) NOT NULL,
  Zip CHAR(6),
  State CHAR(2),
  City VARCHAR(20),
  Country VARCHAR(20)
 
);

-- create
CREATE TABLE Guests (
   ID INTEGER PRIMARY KEY,
   AddressID INTEGER,
  FOREIGN KEY (ID) REFERENCES Addresses(ID),
FirstName VARCHAR(20),
LastName VARCHAR(20),
Phone VARCHAR(20)
);

-- create
CREATE TABLE RoomType (
  RoomTypeID INTEGER PRIMARY KEY,
  RoomTypeName VARCHAR(20),
  StandardOccupancy INTEGER(3),
  MaximumOccupancy INTEGER(3),
  Price DECIMAL(10,2)
);

-- create
CREATE TABLE Room_Amenities (
   RoomAmenitiesID INTEGER PRIMARY KEY,
   RoomID INTEGER (5),
  AmenID INTEGER (10)
 
);

-- create
CREATE TABLE Room (
   RoomID INTEGER PRIMARY KEY,
   RoomTypeID INTEGER,
   AddressID INTEGER,
   RoomAmenitiesID INTEGER,
   ADA BOOLEAN,
   PricesegmentID CHAR(30),
  #FOREIGN KEY (ID) REFERENCES Reservations(ID),
  FOREIGN KEY (RoomTypeID) REFERENCES RoomType(RoomTypeID),
  FOREIGN KEY (RoomAmenitiesID) REFERENCES Room_Amenities(RoomAmenitiesID)
);

CREATE TABLE Reservations (
  ID INTEGER PRIMARY KEY AUTO_INCREMENT,
  GuestID INTEGER,
  RoomID INTEGER,
  -- FOREIGN KEY (GuestID) REFERENCES Guests(ID),
--   FOREIGN KEY (RoomID) REFERENCES Room(RoomID),
  reservation_start_date DATE,
  reservation_end_date DATE,
  adult INT(3),
  children INT(3),
  price Decimal(10,2)
);



CREATE TABLE Amenities (
  RoomAmenitiesID INTEGER primary key AUTO_INCREMENT,
  AmenityType CHAR(20),
  Price INTEGER
);
