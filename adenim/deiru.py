def get_item(self, item_id):
    """Gets an item.

    Args:
        item_id: The ID of the item to get.

    Returns:
        The item.

    Raises:
        ApiError: If the request fails.
    """

    url = "%s/items/%s" % (self.base_url, item_id)
    result = self._make_request(url, "GET")
    return result
