--
-- ���� ������������ � ������� SQLiteStudio v3.3.3 � �� ��� 12 16:47:14 2022
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: users
CREATE TABLE users (id TEXT PRIMARY KEY, username TEXT, email TEXT, phone TEXT);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
