"""How Bonds Are Priced: coupons, yields and the present value of payments."""
CODE = "business4_bondpricing"
BOOK = {
    "title": "How Bonds Are Priced",
    "subtitle": "Coupons, yields and the present value of payments",
    "chapters": [
        ("What a bond is",
         "A bond is a loan. The buyer lends money to a government or a company. The borrower promises regular interest payments and repayment of the face value on a set date. The face value is also called the par value."),
        ("The coupon",
         "The coupon is the fixed interest payment, usually once or twice a year, set as a percentage of face value. A bond with a 5% coupon and a face value of 1,000 pays 50 a year. The coupon is fixed when the bond is issued."),
        ("Price moves against yield",
         "After issue, a bond's price changes as market rates change. When rates rise, existing bonds with lower coupons look less attractive, so their prices fall. When rates fall, their prices rise. Price and yield move in opposite directions."),
        ("Present value",
         "A payment received in the future is worth less today, because money held now can earn interest. The price of a bond is the sum of its future payments, each discounted at the market rate. Adding these discounted payments gives the fair price."),
        ("Premium and discount",
         "A bond sells at a premium when its price is above face value. This tends to happen when its coupon is higher than market rates. It sells at a discount when its price is below face value. At maturity the price returns to face value."),
        ("Yield to maturity",
         "Yield to maturity is the single rate that makes the present value of all the payments equal the price paid. It includes the coupons and any gain or loss from buying above or below face value. Quotes often show it so that buyers can compare bonds."),
    ],
    "test": [
        ("What is the coupon of a bond?",
         [("a", "Its fixed interest payment"), ("b", "Its market price"), ("c", "Its credit rating"), ("d", "The date it was sold")], "a"),
        ("What happens to a bond's price when market rates rise?",
         [("a", "It rises too"), ("b", "It stays the same"), ("c", "It falls"), ("d", "It becomes free")], "c"),
        ("What is a bond sold at a premium?",
         [("a", "A price below face value"), ("b", "A price above face value"), ("c", "A price exactly at face value"), ("d", "A bond with no coupon")], "b"),
        ("What does present value mean?",
         [("a", "Future money is worth more today"), ("b", "Future payments are worth less today, discounted at the market rate"), ("c", "Payments are free"), ("d", "Interest is paid only once")], "b"),
        ("What is yield to maturity?",
         [("a", "The coupon paid in the first year"), ("b", "The rate that makes the present value of all payments equal the price paid"), ("c", "The face value"), ("d", "The rating of the borrower")], "b"),
    ],
}
