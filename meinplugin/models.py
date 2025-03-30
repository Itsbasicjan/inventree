from django.db import models
from django.utils.translation import gettext_lazy as _
from part.models import Part
from company.models import Company

class CustomerAllocation(models.Model):
    part = models.ForeignKey(
        Part,
        on_delete=models.CASCADE,
        verbose_name=_("Teil"),
        help_text=_("Ausgewähltes Inventarteil")
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Menge"),
        help_text=_("Zuzuweisende Menge")
    )
    customer = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name=_("Kunde"),
        help_text=_("Zielkunde für die Zuweisung")
    )
    start_date = models.DateTimeField(
        verbose_name=_("Startdatum")
    )
    end_date = models.DateTimeField(
        verbose_name=_("Enddatum")
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("Notizen")
    )

    class Meta:
        verbose_name = _("Bestandszuweisung")
        verbose_name_plural = _("Bestandszuweisungen")
        permissions = [
            ("view_customerallocation", _("Kann Bestandszuweisungen einsehen")),
            ("change_customerallocation", _("Kann Bestandszuweisungen ändern"))
        ]

    def __str__(self):
        return f"{self.part.name} -> {self.customer.name} ({self.start_date})"