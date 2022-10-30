


from app.unemployment import format_pct





def test_percent_sign_formatting():

    assert format_pct(3.65554) == '3.66%'

    assert format_pct(25.4) == '25.40%'
