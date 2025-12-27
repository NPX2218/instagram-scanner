# --------------------------#
# IMPORTING MODULES
# --------------------------#

import json
import os
from typing import Any, Dict, List, Optional, Union

# --------------------------#
# HELPER FUNCTIONS
# --------------------------#


def load_json(filepath: str) -> Union[Dict[str, Any], List[Any]]:
    """
    Safely load JSON from a file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        Union[Dict[str, Any], List[Any]]: Parsed JSON content (dict or list).

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_usernames(
    data: Union[Dict[str, Any], List[Dict[str, Any]]],
    key: Optional[str] = None
) -> List[str]:

    usernames = []

    # If data is a dict and has a key (like "relationships_following")
    source = data.get(key, data) if isinstance(data, dict) else data

    for item in source:
        if not isinstance(item, dict):
            continue

        # 1. NEW FORMAT → username stored in "title"
        title = item.get("title")
        if isinstance(title, str) and title.strip():
            usernames.append(title.strip())
            continue

        # 2. OLD FORMAT → username stored in string_list_data -> value
        sl = item.get("string_list_data")
        if isinstance(sl, list) and len(sl) > 0:
            entry = sl[0]

            # old export "value"
            if "value" in entry:
                usernames.append(entry["value"])
                continue

            # If value missing, extract from href (/username or /_u/username)
            href = entry.get("href")
            if isinstance(href, str):
                username = href.rstrip('/').split('/')[-1]
                usernames.append(username)
                continue

    return usernames

# --------------------------#
# MAIN SCRIPT
# --------------------------#


if __name__ == "__main__":
    try:
        # Load data
        following_data: Union[Dict[str, Any], List[Any]
                              ] = load_json("files/following.json")
        followers_data: Union[Dict[str, Any], List[Any]
                              ] = load_json("files/followers_1.json")

        # Extract usernames
        following_list: List[str] = extract_usernames(
            following_data, key="relationships_following")
        followers_list: List[str] = extract_usernames(followers_data)

        # Compute difference
        not_following_back: List[str] = sorted(
            set(following_list) - set(followers_list))

        print("People you follow who don't follow you back:")

        for username in not_following_back:
            print(username)

    except Exception as e:
        print(f"Error: {e}")
