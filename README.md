`barabbas`, a devout Christian in `DALnet`, claimed that he pays `10%` of his
total money (income and savings) every year.  So, I thought, why not simulate
him, and offer him free, tax-exempt, and Halal consultancy services?

Parameters:

    * Number of income channels.
    * Bandwidth of income channels (money gained from each income channel).
    * Total savings.
    * Expenses (stuff he spends to live).

For simplicity, we will assume that:

    * Each income channel brings a constant annual revenue.  IMO there is
      really no point in not following this assumption for the purpose of this
      simulation.

Reduction:

    * Since the `10%` tithe is applied on all income channels, and since each
      channel is assumed to have a constant income a year, we can
      mathematically combine them into a single bit channel that the `10%` is
      applied to.  Makes no difference, just mathematically simpler.

    * So, parameters become:
        * `INCOME`: Bandwidth of the _aggregated_ income channels.
        * `EXPENSES`: Bandwidth of the _aggregated_ expenses (except tithes).
        * `TITHES = 10%`: Bandwidth of the tithes.
