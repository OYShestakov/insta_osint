--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Ср янв 12 16:47:14 2022
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: users
CREATE TABLE users (id TEXT PRIMARY KEY, username TEXT, email TEXT, phone TEXT);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
