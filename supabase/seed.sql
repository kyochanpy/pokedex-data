CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    "order" INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    genus VARCHAR(255) NOT NULL,
    image_key VARCHAR(255) NOT NULL,
    dot_image_key VARCHAR(255) NOT NULL,
    height INT NOT NULL,
    weight INT NOT NULL,
    flavor_text TEXT NOT NULL
);

CREATE TABLE types (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE pokemon_type (
    pokemon_id INT,
    type_id INT,
    PRIMARY KEY (pokemon_id, type_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemons(id),
    FOREIGN KEY (type_id) REFERENCES types(id)
);

CREATE TABLE photos (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    pokemon_id INT NOT NULL,
    image_key VARCHAR(255) NOT NULL,
    datetime TIMESTAMP NOT NULL,
    latitude DOUBLE PRECISION NOT NULL,
    longitude DOUBLE PRECISION NOT NULL,
    address VARCHAR(255),
    FOREIGN KEY (pokemon_id) REFERENCES pokemons(id)
);

CREATE TABLE users_pokemons (
    user_id VARCHAR(255),
    pokemon_id INT,
    PRIMARY KEY (user_id, pokemon_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemons(id)
);

CREATE TABLE users_photos (
    user_id VARCHAR(255),
    photo_id VARCHAR(255),
    PRIMARY KEY (user_id, photo_id),
    FOREIGN KEY (photo_id) REFERENCES photos(id)
);

CREATE TABLE pokemons_photos (
    pokemon_id INT,
    photo_id VARCHAR(255),
    PRIMARY KEY (pokemon_id, photo_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemons(id),
    FOREIGN KEY (photo_id) REFERENCES photos(id)
);


insert into storage.buckets
    (id, name, public)
values
    ('images', 'images', true);

CREATE POLICY "images_select" ON storage.objects FOR SELECT TO anon USING (bucket_id = 'images');

CREATE POLICY "images_insert" ON storage.objects FOR INSERT TO anon WITH CHECK (bucket_id = 'images');

CREATE POLICY "images_update" ON storage.objects FOR UPDATE TO anon USING (bucket_id = 'images');

CREATE POLICY "images_delete" ON storage.objects FOR DELETE TO anon USING (bucket_id = 'images');

CREATE OR REPLACE FUNCTION list_pokemons(offset_num int)
RETURNS TABLE (
    "order" INT,
    name VARCHAR,
    dot_image_key VARCHAR,
    types VARCHAR[]
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        p."order",
        p.name,
        p.dot_image_key,
        ARRAY_AGG(t.name ORDER BY t.id) AS types
    FROM
        pokemons p
    LEFT JOIN
        pokemon_type pt ON p.id = pt.pokemon_id
    LEFT JOIN
        types t ON pt.type_id = t.id
    GROUP BY
        p.id
    ORDER BY
        p."order"
    limit
        20
    offset
        offset_num;
END;
$$ LANGUAGE plpgsql;

