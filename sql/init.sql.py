CREATE TABLE companies (
    Name TEXT PRIMARY KEY,
    Employees INTEGER,
    Country TEXT,
    Masked_URL TEXT,
    created_at TIMESTAMP
)
;

INSERT INTO companies (Name, Employees, Country, Masked_URL, created_at)
VALUES
    ('Walmart', 2100000, 'USA', 'https://www[.]walmart[.]com', datetime('now', '-' || ABS(RANDOM() % 40) || ' days', '-' || ABS(RANDOM() % 86400) || ' seconds')),
    ('Volkswagen', 656134, 'Germany', 'https://www[.]vw[.]com/en[.]html', datetime('now', '-' || ABS(RANDOM() % 40) || ' days', '-' || ABS(RANDOM() % 86400) || ' seconds')),
    ('PetroChina', 398440, 'China', 'https://www[.]petrochina[.]com[.]cn/ptr/', datetime('now', '-' || ABS(RANDOM() % 40) || ' days', '-' || ABS(RANDOM() % 86400) || ' seconds')),
    ('GuitarQ', 666, 'Germany', 'https://guitar-quest[.]com/', datetime('now', '-' || ABS(RANDOM() % 40) || ' days', '-' || ABS(RANDOM() % 86400) || ' seconds')),
    ('HDTV', 666, 'USA', 'https://hdtv9[.]com/', datetime('now', '-' || ABS(RANDOM() % 40) || ' days', '-' || ABS(RANDOM() % 86400) || ' seconds'));

;

CREATE TABLE world_companies (
    Name TEXT PRIMARY KEY,
    Employees INTEGER,
    Country TEXT,
    Filtered_URL TEXT,
    created_at TIMESTAMP
)
;