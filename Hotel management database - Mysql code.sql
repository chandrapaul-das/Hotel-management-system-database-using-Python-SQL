#Creating a database
create database hotel; 

#Calling the database
use hotel;             

#Creating the tables where the customer details and booking details are stored for room booking, banquet booking and picnic spot booking resp.
create table customer( ID varchar(50), name varchar(50), age varchar(50), gender varchar(50), ph varchar(50), address varchar(50), persons varchar(50), email varchar(50), check_in date, duration varchar(50), uid varchar(50), code varchar(50));
create table banquet_book(name varchar(50), ph varchar(50), email varchar(50),address varchar(100), guests integer, booking_date date, duration integer, descript varchar(500), uid varchar(50), hall varchar(50));
create table picnic_book(name varchar(50), ph varchar(50), email varchar(50), address varchar(50), guests varchar(50), book_date date, uid varchar(50));

#Creating the tables where the dates in which rooms are booked are stored for Guest suite, Deluxe suite, Premier suite and Executive suite resp. 
create table G_avail( no_101 date, no_102 date, no_103 date, no_104 date, no_105 date, no_106 date, no_107 date, no_108 date, no_109 date, no_110 date, no_111 date, no_112 date, no_113 date, no_114 date, no_115 date, no_116 date, no_117 date, no_118 date, no_119 date, no_120 date);
create table D_avail( no_101 date, no_102 date, no_103 date, no_104 date, no_105 date, no_106 date, no_107 date, no_108 date, no_109 date, no_110 date, no_111 date, no_112 date, no_113 date, no_114 date, no_115 date);
create table P_avail( no_101 date, no_102 date, no_103 date, no_104 date, no_105 date, no_106 date, no_107 date, no_108 date, no_109 date, no_110 date, no_111 date, no_112 date, no_113 date, no_114 date, no_115 date);
create table E_avail( no_101 date, no_102 date, no_103 date, no_104 date, no_105 date);

#Creating the tables where the dates in which banquets are booked are stored for The sonnet banquet, Arunodaya hall and The bonvoy banquet resp. 
create table S_avail(booked date);
create table A_avail(booked date);
create table B_avail(booked date);

#Creating the tables where the date in which picnic spot is booked is stored.
create table picnic_avail(booked date);