import logging
import re


class CreditCardFilter(logging.Filter):
    """Considers any sequence of digits which fits pattern like this as a
    credit card number and filter out it from log.
    """

    def filter(self, record):
        record.msg = re.sub(
            r"\d{4}[\s-]*\d{4}[\s-]*\d{4}[\s-]*\d{4}",
            "XXXX-XXXX-XXXX-XXXX",
            record.msg
        )
        return True
