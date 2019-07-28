-- CREATE DATABASE GreenButcher;

-- USE GreenButcher;

-- CREATE TABLE Products
-- 	(id INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(30) UNIQUE NOT NULL,
--     description VARCHAR(420),
--     price TINYINT NOT NULL,
--     img_url VARCHAR(1000),
--     category INT NOT NULL,
--     favorite BOOL NOT NULL DEFAULT FALSE,
--     FOREIGN KEY(category) REFERENCES Categories(id)
--     );

-- CREATE TABLE Categories
-- 	(id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(20) NOT NULL
--     );

-- INSERT INTO Categories (name) VALUES
-- 	('Main Dishes'),
--     ('Side Dishes');

-- INSERT INTO Products (title, description, price, img_url, category) VALUES
-- 	('Green Butcher Burger', 'A seasoned Beyond Burger patty served in a bun with onion, tomato, lettuce and pickles', 35, 'https://scontent.ftlv2-1.fna.fbcdn.net/v/t1.0-9/67182170_10217709987574646_7144317658945552384_n.jpg?_nc_cat=103&_nc_oc=AQkoLawqryVIszMR9RyFfu8ZONEUqjYMt6MNi1cmqlF0GBo2gF3bI793r2ii_k2x8iAxE2zwBLwb4zoXL4DIFyCI&_nc_ht=scontent.ftlv2-1.fna&oh=34d30ba8b9d89da39e71de30b6ce0ad7&oe=5DE52EE5', 1),
--     ('Beyond Burger', 'A Beyond Burger patty served in a bun with onion, tomato, lettuce and pickles', 35, 'https://scontent.ftlv2-1.fna.fbcdn.net/v/t1.0-9/66420976_10214212292925809_262668431612968960_n.jpg?_nc_cat=110&_nc_oc=AQnyNBZuWVJhJi3tWXxO8LuJA9ju5IdTijA0IpRtT5fg0yczy3kU07-IxSBRQCsnErJqYZgnAbG-liuSKTkM0RMo&_nc_ht=scontent.ftlv2-1.fna&oh=6e169d9068f17fd348b6a7c3f9445b47&oe=5DEAEC1A', 1),
--     ('Hot Dog in a Bun', 'A hot dog in a bun, lemon aioli, sauerkraut with arisa', 35, 'https://scontent.ftlv2-1.fna.fbcdn.net/v/t1.0-9/61439547_10220069627990086_4495336024393646080_n.jpg?_nc_cat=102&_nc_oc=AQmhCcr72BojQFu09HURfUIP6V0zGiG5Vo58Wo-6uNcTpfqRsSTBxkSVija8HkMmNH2lRK5hcXl_t2rJ_DtjG9UQ&_nc_ht=scontent.ftlv2-1.fna&oh=5b210d97ff78773adc343f6fb3ab42ba&oe=5DB3AA2B', 1),
--     ('Arayes', 'A pita bread stuffed with seasoned ground Beyond Meat, tomato salad on the side', 35, 'https://scontent.ftlv2-1.fna.fbcdn.net/v/t1.0-9/61316479_10220069628310094_8041213792215891968_n.jpg?_nc_cat=106&_nc_oc=AQnGfUFGK10piqw1daXK3FEu0xPXtysDG0uHkySAA3jYyacdRpi3tWAmxpCD8JNLVVp-Vimxg3I3oHhTS5nNgaBo&_nc_ht=scontent.ftlv2-1.fna&oh=1e09a6fb5a4ee1c6df707cca05d7cf94&oe=5DAB3E8A', 1),
--     ('Crispy Onion', 'Deep fried coated onion rings', 15, 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/OnionRings.JPG/800px-OnionRings.JPG', 2),
--     ('Seasoned Fries', 'French fries with seasoning', 15, 'https://vegout.co.il/uploads/reviews_images/12158/1.jpg', 2);

select * from Products;

ALTER TABLE `Products` CHANGE COLUMN `desc` `description` VARCHAR(420);



describe Products;

DELETE FROM Products WHERE id = 19;