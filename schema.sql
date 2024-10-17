BEGIN;
--
-- Create model NewsletterSubscriber
--
CREATE TABLE "home_newslettersubscriber" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "email" varchar(254) NOT NULL UNIQUE, "signup_date" datetime NOT NULL, "is_active" bool NOT NULL);
COMMIT;
BEGIN;
--
-- Create model Order
--
CREATE TABLE "checkout_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_number" varchar(32) NOT NULL, "full_name" varchar(50) NOT NULL, "email" varchar(254) NOT NULL, "phone_number" varchar(20) NOT NULL, "country" varchar(40) NOT NULL, "postcode" varchar(20) NULL, "town_or_city" varchar(40) NOT NULL, "street_address1" varchar(80) NOT NULL, "street_address2" varchar(80) NULL, "county" varchar(80) NULL, "date" datetime NOT NULL, "delivery_cost" decimal NOT NULL, "order_total" decimal NOT NULL, "grand_total" decimal NOT NULL);
--
-- Create model OrderLineItem
--
CREATE TABLE "checkout_orderlineitem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "product_size" varchar(2) NULL, "quantity" integer NOT NULL, "lineitem_total" decimal NOT NULL, "order_id" bigint NOT NULL REFERENCES "checkout_order" ("id") DEFERRABLE INITIALLY DEFERRED, "product_id" bigint NOT NULL REFERENCES "products_product" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "checkout_orderlineitem_order_id_b4cfbe6b" ON "checkout_orderlineitem" ("order_id");
CREATE INDEX "checkout_orderlineitem_product_id_739c699d" ON "checkout_orderlineitem" ("product_id");
COMMIT;
BEGIN;
--
-- Create model Category
--
CREATE TABLE "products_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(254) NOT NULL, "friendly_name" varchar(254) NULL);
--
-- Create model Product
--
CREATE TABLE "products_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "sku" varchar(254) NULL, "name" varchar(254) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "image_url" varchar(1024) NULL, "image" varchar(100) NULL, "category_id" bigint NULL REFERENCES "products_category" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "products_product_category_id_9b594869" ON "products_product" ("category_id");
COMMIT;
BEGIN;
--
-- Create model UserProfile
--
CREATE TABLE "profiles_userprofile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "default_phone_number" varchar(20) NULL, "default_country" varchar(2) NULL, "default_postcode" varchar(20) NULL, "default_town_or_city" varchar(40) NULL, "default_street_address1" varchar(80) NULL, "default_street_address2" varchar(80) NULL, "default_county" varchar(80) NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
COMMIT;
BEGIN;
--
-- Add field original_bag to order
--
CREATE TABLE "new__checkout_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "original_bag" text NOT NULL, "order_number" varchar(32) NOT NULL, "full_name" varchar(50) NOT NULL, "email" varchar(254) NOT NULL, "phone_number" varchar(20) NOT NULL, "country" varchar(40) NOT NULL, "postcode" varchar(20) NULL, "town_or_city" varchar(40) NOT NULL, "street_address1" varchar(80) NOT NULL, "street_address2" varchar(80) NULL, "county" varchar(80) NULL, "date" datetime NOT NULL, "delivery_cost" decimal NOT NULL, "order_total" decimal NOT NULL, "grand_total" decimal NOT NULL);
INSERT INTO "new__checkout_order" ("id", "order_number", "full_name", "email", "phone_number", "country", "postcode", "town_or_city", "street_address1", "street_address2", "county", "date", "delivery_cost", "order_total", "grand_total", "original_bag") SELECT "id", "order_number", "full_name", "email", "phone_number", "country", "postcode", "town_or_city", "street_address1", "street_address2", "county", "date", "delivery_cost", "order_total", "grand_total", '' FROM "checkout_order";
DROP TABLE "checkout_order";
ALTER TABLE "new__checkout_order" RENAME TO "checkout_order";
--
-- Add field stripe_pid to order
--
CREATE TABLE "new__checkout_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_number" varchar(32) NOT NULL, "full_name" varchar(50) NOT NULL, "email" varchar(254) NOT NULL, "phone_number" varchar(20) NOT NULL, "country" varchar(40) NOT NULL, "postcode" varchar(20) NULL, "town_or_city" varchar(40) NOT NULL, "street_address1" varchar(80) NOT NULL, "street_address2" varchar(80) NULL, "county" varchar(80) NULL, "date" datetime NOT NULL, "delivery_cost" decimal NOT NULL, "order_total" decimal NOT NULL, "grand_total" decimal NOT NULL, "original_bag" text NOT NULL, "stripe_pid" varchar(254) NOT NULL);
INSERT INTO "new__checkout_order" ("id", "order_number", "full_name", "email", "phone_number", "country", "postcode", "town_or_city", "street_address1", "street_address2", "county", "date", "delivery_cost", "order_total", "grand_total", "original_bag", "stripe_pid") SELECT "id", "order_number", "full_name", "email", "phone_number", "country", "postcode", "town_or_city", "street_address1", "street_address2", "county", "date", "delivery_cost", "order_total", "grand_total", "original_bag", '' FROM "checkout_order";
DROP TABLE "checkout_order";
ALTER TABLE "new__checkout_order" RENAME TO "checkout_order";
COMMIT;
BEGIN;
--
-- Alter field country on order
--
CREATE TABLE "new__checkout_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "country" varchar(2) NOT NULL, "order_number" varchar(32) NOT NULL, "full_name" varchar(50) NOT NULL, "email" varchar(254) NOT NULL, "phone_number" varchar(20) NOT NULL, "postcode" varchar(20) NULL, "town_or_city" varchar(40) NOT NULL, "street_address1" varchar(80) NOT NULL, "street_address2" varchar(80) NULL, "county" varchar(80) NULL, "date" datetime NOT NULL, "delivery_cost" decimal NOT NULL, "order_total" decimal NOT NULL, "grand_total" decimal NOT NULL, "original_bag" text NOT NULL, "stripe_pid" varchar(254) NOT NULL);
INSERT INTO "new__checkout_order" ("id", "order_number", "full_name", "email", "phone_number", "postcode", "town_or_city", "street_address1", "street_address2", "county", "date", "delivery_cost", "order_total", "grand_total", "original_bag", "stripe_pid", "country") SELECT "id", "order_number", "full_name", "email", "phone_number", "postcode", "town_or_city", "street_address1", "street_address2", "county", "date", "delivery_cost", "order_total", "grand_total", "original_bag", "stripe_pid", "country" FROM "checkout_order";
DROP TABLE "checkout_order";
ALTER TABLE "new__checkout_order" RENAME TO "checkout_order";
COMMIT;
BEGIN;
--
-- Add field user_profile to order
--
ALTER TABLE "checkout_order" ADD COLUMN "user_profile_id" bigint NULL REFERENCES "profiles_userprofile" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "checkout_order_user_profile_id_949184a7" ON "checkout_order" ("user_profile_id");
COMMIT;
BEGIN;
--
-- Change Meta options on category
--
-- (no-op)
--
-- Remove field image_url from product
--
ALTER TABLE "products_product" DROP COLUMN "image_url";
--
-- Add field gender to product
--
CREATE TABLE "new__products_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "gender" varchar(10) NOT NULL, "sku" varchar(254) NULL, "name" varchar(254) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "image" varchar(100) NULL, "category_id" bigint NULL REFERENCES "products_category" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__products_product" ("id", "sku", "name", "description", "price", "image", "category_id", "gender") SELECT "id", "sku", "name", "description", "price", "image", "category_id", 'Unisex' FROM "products_product";
DROP TABLE "products_product";
ALTER TABLE "new__products_product" RENAME TO "products_product";
CREATE INDEX "products_product_category_id_9b594869" ON "products_product" ("category_id");
COMMIT;
BEGIN;
--
-- Add field detail_image to product
--
ALTER TABLE "products_product" ADD COLUMN "detail_image" varchar(100) NULL;
COMMIT;
BEGIN;
--
-- Add field rating to product
--
ALTER TABLE "products_product" ADD COLUMN "rating" decimal NULL;
COMMIT;
BEGIN;
--
-- Alter field gender on product
--
CREATE TABLE "new__products_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "gender" varchar(6) NULL, "sku" varchar(254) NULL, "name" varchar(254) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "image" varchar(100) NULL, "category_id" bigint NULL REFERENCES "products_category" ("id") DEFERRABLE INITIALLY DEFERRED, "detail_image" varchar(100) NULL, "rating" decimal NULL);
INSERT INTO "new__products_product" ("id", "sku", "name", "description", "price", "image", "category_id", "detail_image", "rating", "gender") SELECT "id", "sku", "name", "description", "price", "image", "category_id", "detail_image", "rating", "gender" FROM "products_product";
DROP TABLE "products_product";
ALTER TABLE "new__products_product" RENAME TO "products_product";
CREATE INDEX "products_product_category_id_9b594869" ON "products_product" ("category_id");
COMMIT;
BEGIN;
--
-- Create model Size
--
CREATE TABLE "products_size" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "size" varchar(10) NOT NULL);
--
-- Add field sizes to product
--
CREATE TABLE "products_product_sizes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "product_id" bigint NOT NULL REFERENCES "products_product" ("id") DEFERRABLE INITIALLY DEFERRED, "size_id" bigint NOT NULL REFERENCES "products_size" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "products_product_sizes_product_id_size_id_1c8c3d5d_uniq" ON "products_product_sizes" ("product_id", "size_id");
CREATE INDEX "products_product_sizes_product_id_7cf7aa08" ON "products_product_sizes" ("product_id");
CREATE INDEX "products_product_sizes_size_id_e0cab160" ON "products_product_sizes" ("size_id");
COMMIT;
BEGIN;
--
-- Add field image_url to product
--
ALTER TABLE "products_product" ADD COLUMN "image_url" varchar(1024) NULL;
COMMIT;
BEGIN;
--
-- Remove field image_url from product
--
ALTER TABLE "products_product" DROP COLUMN "image_url";
--
-- Alter field image on product
--
CREATE TABLE "new__products_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "image" varchar(255) NULL, "sku" varchar(254) NULL, "name" varchar(254) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "category_id" bigint NULL REFERENCES "products_category" ("id") DEFERRABLE INITIALLY DEFERRED, "gender" varchar(6) NULL, "detail_image" varchar(100) NULL, "rating" decimal NULL);
INSERT INTO "new__products_product" ("id", "sku", "name", "description", "price", "category_id", "gender", "detail_image", "rating", "image") SELECT "id", "sku", "name", "description", "price", "category_id", "gender", "detail_image", "rating", "image" FROM "products_product";
DROP TABLE "products_product";
ALTER TABLE "new__products_product" RENAME TO "products_product";
CREATE INDEX "products_product_category_id_9b594869" ON "products_product" ("category_id");
COMMIT;
BEGIN;
--
-- Alter field detail_image on product
--
CREATE TABLE "new__products_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "detail_image" varchar(255) NULL, "sku" varchar(254) NULL, "name" varchar(254) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "image" varchar(255) NULL, "category_id" bigint NULL REFERENCES "products_category" ("id") DEFERRABLE INITIALLY DEFERRED, "gender" varchar(6) NULL, "rating" decimal NULL);
INSERT INTO "new__products_product" ("id", "sku", "name", "description", "price", "image", "category_id", "gender", "rating", "detail_image") SELECT "id", "sku", "name", "description", "price", "image", "category_id", "gender", "rating", "detail_image" FROM "products_product";
DROP TABLE "products_product";
ALTER TABLE "new__products_product" RENAME TO "products_product";
CREATE INDEX "products_product_category_id_9b594869" ON "products_product" ("category_id");
COMMIT;
BEGIN;
--
-- Add field tags to product
--
-- (no-op)
COMMIT;
BEGIN;
--
-- Alter field tags on product
--
-- (no-op)
COMMIT;
BEGIN;
--
-- Alter field id on newslettersubscriber
--
CREATE TABLE "new__home_newslettersubscriber" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "email" varchar(254) NOT NULL UNIQUE, "signup_date" datetime NOT NULL, "is_active" bool NOT NULL);
INSERT INTO "new__home_newslettersubscriber" ("email", "signup_date", "is_active", "id") SELECT "email", "signup_date", "is_active", "id" FROM "home_newslettersubscriber";
DROP TABLE "home_newslettersubscriber";
ALTER TABLE "new__home_newslettersubscriber" RENAME TO "home_newslettersubscriber";
COMMIT;
BEGIN;
--
-- Create model CustomerTestimonial
--
CREATE TABLE "home_customertestimonial" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "testimonial" text NOT NULL, "rating" integer NOT NULL, "date" date NOT NULL);
COMMIT;
BEGIN;
--
-- Create model FAQ
--
CREATE TABLE "home_faq" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question" varchar(200) NOT NULL, "answer" text NOT NULL, "category" varchar(100) NOT NULL, "order" integer NOT NULL);
COMMIT;
BEGIN;
--
-- Create model ContactSubmission
--
CREATE TABLE "home_contactsubmission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "email" varchar(254) NOT NULL, "message" text NOT NULL, "date_submitted" datetime NOT NULL);
COMMIT;
