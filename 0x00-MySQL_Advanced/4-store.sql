-- Creates a trigger that decreases the quantity of an item after adding a new order.

DROP TRIGGER IF EXISTS qty_reducer;
DELIMITER $$
CREATE TRIGGER IF NOT EXISTS qty_reducer
AFTER INSERT ON orders 
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END$$
DELIMITER ;
