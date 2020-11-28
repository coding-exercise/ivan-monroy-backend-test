import random

import pytest

from utils import *


def test_language():
    assert len(alphabet) == len(foo_letters) + len(bar_letters)
    assert set(alphabet) == set(foo_letters).union(set(bar_letters))


def generate_preposition():
    alphabet_minus_u = alphabet.copy()
    alphabet_minus_u.remove('u')
    foo_letters_minus_u = foo_letters.copy()
    foo_letters_minus_u.remove('u')
    word = ''.join(random.choice(alphabet_minus_u) for i in range(5))
    word += random.choice(foo_letters_minus_u)
    return word


@pytest.mark.parametrize('preposition',
                         [generate_preposition() for i in range(50)])
def test_preposition(preposition):
    assert is_preposition(preposition)


def generate_verb():
    # We'll only generate strings of length less or equal to 20
    word_length = random.choice(range(5, 20))
    word = ''.join(random.choice(alphabet) for i in range(word_length))
    word += random.choice(bar_letters)
    return word


@pytest.mark.parametrize('verb', [generate_verb() for i in range(50)])
def test_verb(verb):
    assert is_verb(verb)


def generate_subjunctive_verb():
    # We'll only generate strings of length less or equal to 20
    word_length = random.choice(range(4, 20))
    word = ''.join(random.choice(alphabet) for i in range(word_length))
    word = random.choice(bar_letters) + word + random.choice(bar_letters)
    return word


@pytest.mark.parametrize('subjunctive_verb',
                         [generate_subjunctive_verb() for i in range(50)])
def test_subjunctive_verb(subjunctive_verb):
    assert is_subjunctive_verb(subjunctive_verb)


def from_decimal(number):
    base20 = ''
    if number < 20:
        return alphabet[number] + base20
    else:
        return alphabet[number % 20] + from_decimal(number // 20)


@pytest.mark.parametrize('number',
                         [random.randrange(1000000) for i in range(50)])
def test_base_conversion(number):
    base20 = from_decimal(number)
    assert to_decimal(from_decimal(number)) == number
    assert from_decimal(to_decimal(base20)) == base20


@pytest.mark.parametrize('number', [random.randrange(1000) for i in range(50)])
def test_is_pretty(number):
    assert is_pretty_number(from_decimal(3 * (number + 27276)))


def test_vocabulary_list():
    text = [
        'shoce',
        'pq',
        'podciy',
        'nfwh',
        'phfer',
        'epgdc',
        'dgsloqe',
        'do',
        'rhfl',
        'qhmoixw',
        'cmfur',
        'qdrulxogji',
        'whc',
        'ermjdhsx',
        'py',
        'en',
        'yco',
        'ienqm',
        'wjuln',
        'dwuch',
        'qinhmjul',
        'mjxdqfrnlg',
        'iygsex',
        'qihmu',
        'grewyluhfs',
        'ucf',
        'us',
        'xclpedqmi',
        'yrx',
        'qinexwo',
        'qx',
        'rqw',
        'wxflpdn',
        'rsogxd',
        'cpqmxj',
        'lgchqdin',
        'fdw',
        'nwcrus',
        'coj',
        'nj',
        'qplfjnwidg',
        'fwdmslqn',
        'cwj',
        'hysucxdqm',
        'ms',
        'hdmwpe',
        'igxweo',
        'sqflo',
        'ycqlinro',
        'ghu',
        'hgecdfj',
        'mw',
        'xrpmyenq',
        'fgixsr',
        'fpwcnguieh',
        'fclgj',
        'ghepqyd',
        'jxhwe',
        'cejfugn',
        'ujxqh',
        'ihncrl',
        'mlceo',
        'udr',
        'fm',
        'ocxfsjdng',
        'sfoqmd',
        'pdoymnwxei',
        'spqinedf',
        'ql',
        'ncsepfl',
        'icmqsdj',
        'chwjlg',
        'yiq',
        'ifl',
        'syejrqd',
        'lwnepmcg',
        'xlmnfqry',
        'ghlyopuncw',
        'qx',
        'iw',
        'sionpux',
        'cop',
        'dmqpchuyf',
        'ojxfqhernm',
        'ignpeyf',
        'rseoyl',
        'emjocsild',
        'rfimdy',
        'mwd',
        'oewgjfr',
        'uo',
        'irmcunfgx',
        'ylduwpsnh',
        'xrdng',
        'gcxr',
        'ng',
        'prfmjicud',
        'srdueqhgiy',
        'nmodwsqijh',
        'dcnql']
    sort_uniq = [
        'sqflo',
        'spqinedf',
        'sfoqmd',
        'syejrqd',
        'shoce',
        'srdueqhgiy',
        'sionpux',
        'xclpedqmi',
        'xlmnfqry',
        'xrpmyenq',
        'xrdng',
        'ocxfsjdng',
        'oewgjfr',
        'ojxfqhernm',
        'cop',
        'coj',
        'cmfur',
        'cwj',
        'cpqmxj',
        'chwjlg',
        'cejfugn',
        'qx',
        'qplfjnwidg',
        'qhmoixw',
        'ql',
        'qdrulxogji',
        'qinhmjul',
        'qinexwo',
        'qihmu',
        'ncsepfl',
        'nmodwsqijh',
        'nwcrus',
        'nfwh',
        'nj',
        'ng',
        'ms',
        'mw',
        'mwd',
        'mlceo',
        'mjxdqfrnlg',
        'wxflpdn',
        'whc',
        'wjuln',
        'podciy',
        'pq',
        'py',
        'phfer',
        'prfmjicud',
        'pdoymnwxei',
        'fclgj',
        'fm',
        'fwdmslqn',
        'fpwcnguieh',
        'fdw',
        'fgixsr',
        'yco',
        'ycqlinro',
        'ylduwpsnh',
        'yrx',
        'yiq',
        'hysucxdqm',
        'hdmwpe',
        'hgecdfj',
        'en',
        'emjocsild',
        'epgdc',
        'ermjdhsx',
        'lwnepmcg',
        'lgchqdin',
        'jxhwe',
        'rsogxd',
        'rseoyl',
        'rqw',
        'rfimdy',
        'rhfl',
        'do',
        'dcnql',
        'dmqpchuyf',
        'dwuch',
        'dgsloqe',
        'gcxr',
        'ghepqyd',
        'ghlyopuncw',
        'ghu',
        'grewyluhfs',
        'us',
        'uo',
        'ucf',
        'ujxqh',
        'udr',
        'icmqsdj',
        'iw',
        'ifl',
        'iygsex',
        'ihncrl',
        'ienqm',
        'irmcunfgx',
        'igxweo',
        'ignpeyf']
    assert vocabulary_list(text) == sort_uniq


def test_statistics_dictionary():
    text = ['phqy', 'phqy', 'phqy', 'phqy']
    assert build_statistics_dictionary(text) == {
        'prepositions': 0,
        'verbs': 0,
        'subjunctive_verbs': 0,
        'pretty_numbers': 1}
    text = ['phqy', 'phqy', 'phqy', 'phqy', 'hhqy']
    assert build_statistics_dictionary(text) == {
        'prepositions': 0,
        'verbs': 0,
        'subjunctive_verbs': 0,
        'pretty_numbers': 2}
