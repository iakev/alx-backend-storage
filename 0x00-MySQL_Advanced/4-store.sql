-- Creating a tigger after an event
-- creates a trigger to decrease quantity in item table after adding a new order

DELIMITER $$ ;
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items 
	SET quantity = quantity - NEW.number
	WHERE NEW.item_name = name;
END;
$$
