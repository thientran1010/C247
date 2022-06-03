
-- Problem 1
SELECT g.firstname, g.lastname , rs.roomID , r.reservation_start_date, r.reservation_end_date FROM Reservations r
LEFT JOIN Guests g ON r.guestID=g.ID 
LEFT JOIN Room rs on r.RoomID=rs.RoomID
WHERE r.reservation_end_date >= '2023-07-01'
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

