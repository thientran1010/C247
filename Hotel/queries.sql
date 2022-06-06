
-- Problem 1
SELECT g.firstname, g.lastname , rs.roomID , r.reservation_start_date, r.reservation_end_date FROM Reservations r
LEFT JOIN Guests g ON r.guestID=g.ID 
LEFT JOIN Room rs on r.RoomID=rs.RoomID
WHERE r.reservation_end_date <= '2023-07-31'
;

-- Problem 2 
SELECT guests.Lastname, room.RoomID, reservations.reservation_start_date, reservations.reservation_end_date
FROM reservations
INNER JOIN guests ON reservations.GuestID = guests.ID
INNER JOIN room ON room.RoomID = reservations.RoomID
INNER JOIN room_amenities ON room_amenities.RoomID = room.RoomID
INNER JOIN amenities ON amenities.RoomAmenitiesID = room_amenities.AmenID
WHERE amenities.AmenityType='Jacuzzi';

-- Problem 3
select
FirstName,
LastName,
RoomId as 'Room Number',
reservation_start_date as 'Reservation Start Date',
reservation_end_date as 'Reservation End Date',
adult as 'Number of Adults',
children as 'Number of Children',
price as 'Total Price'
from reservations r
left join
guests g
on g.ID = r.GuestID
where
g.ID = 2;

-- Problem 4
select
ro.RoomID as 'Room Number',
re.ID as 'Reservation ID',
reservation_start_date as 'Reservation Start Date',
reservation_end_date as 'Reservation End Date',
price as 'Total Price'
from
rooms ro
left outer join reservations re
on
ro.RoomID = re.RoomID
order by
ro.RoomID asc;

-- Problem 5
select
(adult + children) as 'Total Guests',
ro.RoomID as 'Room Number'
from
reservations re
left join rooms ro
on
ro.RoomId = re.RoomID
where
(adult + children) < 3
and
reservation_start_date >= '2023-04-01'
and
reservation_end_date <= '2023-04-30'
;

-- Problem 6

select
FirstName,
LastName,
count(re.ID) as 'Reservation Count'
from
guests g
inner join
reservations re
on
g.ID = re.guestID
group by
FirstName
order by
3 desc, 2
;

-- Problem 7
select
FirstName,
LastName,
a.Address,
a.State,
a.City,
a.Zip,
a.Country,
Phone as 'Phone Number'
from
guests g
inner join
addresses a
on g.AddressID = a.ID
order by
phone;


