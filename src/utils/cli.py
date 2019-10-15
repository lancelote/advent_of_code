import click


SUPPORTED_YEARS = [
    '2015',
    '2016',
    '2017',
    '2018',
]


class YearType(click.ParamType):
    def convert(self, value, param, ctx):
        if value in SUPPORTED_YEARS:
            return value
        else:
            supported_year = '/'.join(SUPPORTED_YEARS)
            self.fail(f'Expected {supported_year}, got {value}', param, ctx)


class DayType(click.ParamType):
    def convert(self, value, param, ctx):
        try:
            assert int(value) in range(1, 32)
            assert isinstance(value, str)
            return value
        except (TypeError, AssertionError):
            self.fail(f'Expected in range 1-31, got {value}', param, ctx)


class PartType(click.ParamType):
    def convert(self, value, param, ctx):
        formatted_value = value.lower()
        if formatted_value in ['a', 'b']:
            return formatted_value
        else:
            self.fail(f'Expected either A or B, got {value}', param, ctx)


YEAR = YearType()
DAY = DayType()
PART = PartType()

__all__ = ['YEAR', 'DAY', 'PART']
