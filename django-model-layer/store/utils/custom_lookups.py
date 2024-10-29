from django.db.models import Transform, Lookup
from django.db.models import Field, IntegerField


@Field.register_lookup
class NotEqual(Lookup):
    lookup_name = "ne"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return "%s <> %s" % (lhs, rhs), params
    


@IntegerField.register_lookup
class AbsoluteValue(Transform):
    lookup_name = "abs"
    function = "ABS"
    bilateral = True