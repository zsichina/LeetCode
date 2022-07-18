from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            name, domain = email.split("@")
            seen.add(name.split("+")[0].replace(".", "") + "@" + domain)
        return len(seen)
