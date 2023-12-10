from app import parse_wine

def test():
    example_resposne = """Certainly! Here are five recommendations of wines, along with the wineries they come from, for your party tonight:\n1. Château Margaux from Château Margaux (Bordeaux, France) - A renowned winery known for its exceptional red wine, Château Margaux offers a classic Bordeaux blend with elegant flavors of dark fruit, spice, and refined tannins.\n2. Dom Pérignon from Moët & Chandon (Champagne, France) - A luxurious champagne produced by Moët & Chandon, Dom Pérignon showcases finesse and complexity, with notes of citrus, toasted bread, and a delicate effervescence.\n3. Shafer Vineyards Hillside Select from Shafer Vineyards (Napa Valley, California) - Known for their outstanding Cabernet Sauvignon, Shafer Vineyards crafts Hillside Select, a bold and opulent wine with ripe dark fruit flavors, hints of mocha, and velvety tannins.\n4. Cloudy Bay Sauvignon Blanc from Cloudy Bay (Marlborough, New Zealand) - A reputable winery from New Zealand, Cloudy Bay produces a deliciously vibrant and aromatic Sauvignon Blanc. Expect zesty citrus, passionfruit, and herbaceous notes in this refreshing white wine.\n5. Marchesi Antinori Tignanello from Marchesi Antinori (Tuscany, Italy) - Marchesi Antinori is an esteemed Italian winery famous for Tignanello, a Super Tuscan wine. This full-bodied red blend offers rich black fruit flavors, layers of spice, and a velvety texture.\nRemember to consider your guests' preferences and food pairings when deciding on wines for your party. Enjoy your event!"""
    recommendation = parse_wine(example_resposne) 
    for sent in recommendation:
        assert int(sent[0]) in range(1,6)

if __name__ == "__main__":
    test()