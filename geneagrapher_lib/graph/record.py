import functools


@functools.total_ordering
class Record:
    """
    Container class storing record of a mathematician in the graph.
    """

    def __init__(self, name, institution=None, year=None, id=None):
        """
        Record class constructor.

        Parameters:
            name: string containing mathematician's name
            institution: string containing mathematician's institution
                (empty if none)
            year: integer containing year degree was earned
            id: integer containing Math Genealogy Project id value
        """
        self.name = name
        self.institution = institution
        self.year = year
        self.id = id

        # Verify we got the types wanted.
        if not isinstance(self.name, str):
            raise TypeError(
                "Unexpected parameter type: expected string value \
for 'name'"
            )
        if (
            not isinstance(self.institution, str)
            and self.institution is not None
        ):
            raise TypeError(
                "Unexpected parameter type: expected string value \
for 'institution'"
            )
        if not isinstance(self.year, int) and self.year is not None:
            raise TypeError(
                "Unexpected parameter type: expected integer \
value for 'year'"
            )
        if not isinstance(self.id, int) and self.id is not None:
            raise TypeError(
                "Unexpected parameter type: expected integer \
value for 'id'"
            )

    def __eq__(self, r2):
        return self.id == r2.id

    def __lt__(self, r2):
        return self.id < r2.id


    def __str__(self):
        if self.has_institution():
            if self.has_year():
                return "{} \\n{} ({})".format(self.name, self.institution, self.year)
            else:
                return "{} \\n{}".format(self.name, self.institution)
        else:
            if self.has_year():
                return "{} \\n({})".format(self.name, self.year)
            else:
                return self.name

    def has_institution(self):
        """
        Return True if this record has an institution associated with it,
        else False.
        """
        return self.institution is not None

    def has_year(self):
        """
        Return True if this record has a year associated with it, else
        False.
        """
        return self.year is not None
