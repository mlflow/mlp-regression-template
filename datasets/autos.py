import pandas as pd

names = """symboling
normalized-losses
make
fuel-type
aspiration
num-of-doors
body-style
drive-wheels
engine-location
wheel-base
length
width
height
curb-weight
engine-type
num-of-cylinders
engine-size
fuel-system
bore
stroke
compression-ratio
horsepower
peak-rpm
city-mpg
highway-mpg
price""".split(
    "\n"
)

pdf = pd.read_csv("./autos/imports-85.data", header=None, names=names, na_values=["?"])
# Parsed num-of-doors column contains Python `None` values, which causes issues during
# the label encoding portion of transformer fitting where NoneTypes are compared to strings.
# We hackily fix that by imputing with the empty string.
pdf["num-of-doors"] = pdf["num-of-doors"].fillna("")

print(
    f"""

== data preview ==

{pdf.head(5)}

== inferred schema ==

{pdf.dtypes}

== data summary ==

{pdf.describe()}
"""
)

pdf.to_parquet("autos.parquet")
