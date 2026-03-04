"""Connector object for defining common behaviors."""

from abc import ABC, abstractmethod

import pydicom


class Connector(ABC):
    """An abstract interface for a Connector object.

    Args
    ----
        ABC (_type_): derives from Abstract Base Class.
    """

    @abstractmethod
    @classmethod
    def get_instances_by_id(
        cls, identifiers: dict[str, str]
    ) -> list[dict[str, list[pydicom.Dataset]]]:
        """Abstract method to get all instances that match an identifiers query.

        Args
        ----
            identifiers (dict[str, str]): A dictionary containing query ids.

        Returns
        -------
            list[dict[str, list[pydicom.Dataset]]: outer list of patients,
                dict of studies, and a list of corresponding DICOM instances
        """
