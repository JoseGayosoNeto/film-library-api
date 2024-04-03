from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'United States of America'),
    ('CHN', 'China'),
    ('JPN', 'Japan'),
    ('DEU', 'Germany'),
    ('IND', 'India'),
    ('GBR', 'United Kingdom'),
    ('FRA', 'France'),
    ('ITA', 'Italy'),
    ('BRA', 'Brazil'),
    ('CAN', 'Canada'),
    ('RUS', 'Russia'),
    ('KOR', 'South Korea'),
    ('AUS', 'Australia'),
    ('ESP', 'Spain'),
    ('MEX', 'Mexico'),
    ('IDN', 'Indonesia'),
    ('TUR', 'Turkey'),
    ('SAU', 'Saudi Arabia'),
    ('CHE', 'Switzerland'),
    ('NLD', 'Netherlands'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
