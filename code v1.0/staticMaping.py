import staticmaps as mp

def staticmap(targetL,targetR):
    context = mp.Context()
    # context.set_tile_provider(mp.tile_provider_StamenToner)
    context.set_tile_provider(mp.tile_provider_OSM)

    spot = mp.create_latlng( targetL , targetR)

    context.add_object(mp.Marker(spot, color=mp.GREEN, size=6))

    image1 = context.render_pillow(260, 180)
    image1.save("spot.pillow.png")

def staticmapRoute(targetL,targetR, sourceL, sourceR):
    context = mp.Context()
    # context.set_tile_provider(mp.tile_provider_StamenToner)
    context.set_tile_provider(mp.tile_provider_OSM)

    source = mp.create_latlng(sourceL, sourceR)
    destination = mp.create_latlng(targetL, targetR)
    route = [source, destination]

    context.add_object(mp.Line(route, color=mp.BLUE, width=4))

    image1 = context.render_pillow(260, 180)
    image1.save("spot.pillow.png")


