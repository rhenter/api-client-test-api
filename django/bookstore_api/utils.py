import codecs
import os
import re
from json import dumps
from urllib.parse import (parse_qsl, ParseResult, unquote, urlencode, urlparse)

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_stuff.utils import remove_special_characters
from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)


def clean_filename(filename):
    fragment_filename = filename.split('.')
    name = '_'.join(remove_special_characters(
        ''.join(fragment_filename[:-1])).split()).lower()
    ext = fragment_filename[-1]
    return '{}.{}'.format(name, ext)


def get_version():
    current_version = ''
    changes = os.path.join(BASE_DIR, "CHANGES.rst")
    pattern = r'^(?P<version>[0-9]+.[0-9]+(.[0-9]+)?)'
    with codecs.open(changes, encoding='utf-8') as changes:
        for line in changes:
            match = re.match(pattern, line)
            if match:
                current_version = match.group("version")
                break
    return current_version or '0.1.0'


def upload_to(instance, filename, document_type='image'):
    folder = type(instance).__name__.lower()

    root_path = settings.MODEL_STORAGE_ROOT.get(
        folder, '{}s/'.format(document_type))
    filename = clean_filename(filename)

    return os.path.join(*[
        root_path,
        folder,
        str(instance.id),
        filename
    ])


def image_upload_path(instance, filename):
    return upload_to(instance, filename, document_type='image')


def document_upload_path(instance, filename):
    return upload_to(instance, filename, document_type='document')


def invoice_upload_path(instance, filename):
    return upload_to(instance, filename, document_type='invoice')


def get_verbose_timedelta(days):
    years = 0
    months = int(days / 30)
    if months > 12:
        years = int(months / 12)
        months = months - (years * 12)
    return _("{} years and {} months").format(years, months)


def clean_url(url):
    url = unquote(url)
    # Extracting url info
    parsed_url = urlparse(url)
    # Extracting URL arguments from parsed URL
    get_args = parsed_url.query
    # Converting URL arguments to dict
    parsed_get_args = dict(parse_qsl(get_args))
    # Merging URL arguments dict with new params
    parsed_get_args.pop('page', '')

    parsed_get_args.update(
        {k: dumps(v) for k, v in parsed_get_args.items()
         if isinstance(v, (bool, dict))}
    )

    # Converting URL argument to proper query string
    encoded_get_args = urlencode(parsed_get_args, doseq=True)
    # Creating new parsed result object based on provided with new
    # URL arguments. Same thing happens inside of urlparse.
    new_url = ParseResult(
        parsed_url.scheme, parsed_url.netloc, parsed_url.path,
        parsed_url.params, encoded_get_args, parsed_url.fragment
    ).geturl()

    return new_url
