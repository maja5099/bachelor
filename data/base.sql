-- SQLite

-- USERS
CREATE TABLE IF NOT EXISTS users (
    user_id	            	INTEGER NOT NULL UNIQUE,
	first_name	        	TEXT NOT NULL,
	last_name	        	TEXT NOT NULL,
	email	            	TEXT NOT NULL,
	phone					INTEGER NOT NULL UNIQUE,
	username				TEXT NOT NULL UNIQUE,
	password	        	TEXT NOT NULL,
	is_active	        	INTEGER NOT NULL,
	created_at	        	TEXT NOT NULL,
	updated_at	        	TEXT,
	deleted_at	        	TEXT,
	user_roles_user_role_id	INTEGER,	
	PRIMARY KEY(user_id)
) WITHOUT ROWID;


-- CLIPCARDS AND CARDTYPES
CREATE TABLE IF NOT EXISTS clipcards (
	clipcard_id	        INTEGER NOT NULL UNIQUE,
	clipcard_type_id	INTEGER NOT NULL,
	time_used			INTEGER NOT NULL,
	remaining_time	    INTEGER NOT NULL,
	created_at	        TEXT NOT NULL,
	updated_at	        TEXT NOT NULL,
	deleted_at			TEXT,
	is_active			INTEGER NOT NULL,
	PRIMARY KEY(clipcard_id)
) WITHOUT ROWID;


CREATE TABLE IF NOT EXISTS card_types (
	clipcard_type_id	INTEGER NOT NULL UNIQUE,
	clipcard_type_title	TEXT NOT NULL,
	clipcard_type_time	INTEGER NOT NULL,
	clipcard_price		INTEGER NOT NULL,
	PRIMARY KEY(clipcard_type_id)
) WITHOUT ROWID;

INSERT INTO card_types (clipcard_type_id, clipcard_type_title, clipcard_type_time, clipcard_price) VALUES
(1, '10 timer', 10, 7000),
(2, '20 timer', 20, 14000),
(3, '30 timer', 30, 19500);


-- TASKS
CREATE TABLE IF NOT EXISTS tasks (
	task_id	            INTEGER NOT NULL UNIQUE,
	clipcard_id	        INTEGER NOT NULL UNIQUE,
	customer_id			INTEGER NOT NULL UNIQUE,
	task_title			TEXT NOT NULL,
	task_description	TEXT NOT NULL,
	created_at	        TEXT,
	time_spent	        INTEGER NOT NULL,
	PRIMARY KEY(task_id)
) WITHOUT ROWID;


-- PAYMENTS
CREATE TABLE IF NOT EXISTS payments (
	payment_id	        INTEGER NOT NULL UNIQUE,
	user_id				INTEGER NOT NULL,
	clipcard_id	        INTEGER NOT NULL UNIQUE,
	amount_paid	        INTEGER NOT NULL,
	created_at	        TEXT NOT NULL,
	PRIMARY KEY(payment_id)
) WITHOUT ROWID;


-- USER ROLES AND RIGHTS
CREATE TABLE IF NOT EXISTS user_roles (
	user_role_id		INTEGER NOT NULL,
	user_role_title		TEXT NOT NULL,
	PRIMARY KEY(user_role_id)
) WITHOUT ROWID;

INSERT INTO user_roles (user_role_id, user_role_title) VALUES
(1, 'customer'),
(2, 'staff');


CREATE TABLE IF NOT EXISTS customers (
	customer_id			INTEGER NOT NULL UNIQUE,
	user_role_id		INTEGER NOT NULL,
	website_name		TEXT NOT NULL,
	website_url			TEXT NOT NULL,
	PRIMARY KEY(customer_id)
) WITHOUT ROWID;


CREATE TABLE IF NOT EXISTS staff (
	staff_id			INTEGER NOT NULL UNIQUE,
	user_role_id		INTEGER NOT NULL,
	PRIMARY KEY(staff_id)
) WITHOUT ROWID;


CREATE TABLE IF NOT EXISTS user_role_rights (
	right_id			INTEGER NOT NULL UNIQUE,
	user_role_id		INTEGER NOT NULL UNIQUE,
	can_view			INTEGER NOT NULL,
	can_add				INTEGER NOT NULL,
	can_edit			INTEGER NOT NULL,
	can_delete			INTEGER NOT NULL,
	PRIMARY KEY(user_role_id)
) WITHOUT ROWID;

INSERT INTO user_role_rights (right_id, user_role_id, can_view, can_add, can_edit, can_delete) VALUES
(1, '1', '1', '0', '0', '0'),
(2, '2', '1', '1', '1', '1');

-- MESSAGES
CREATE TABLE IF NOT EXISTS messages (
	message_id			INTEGER NOT NULL UNIQUE,
	user_id				INTEGER NOT NULL,
	message_subject		TEXT NOT NULL,
	message_text		TEXT NOT NULL,
	message_file		TEXT,
	created_at			TEXT NOT NULL,
	deleted_at			TEXT,
	PRIMARY KEY(message_id)
) WITHOUT ROWID;
