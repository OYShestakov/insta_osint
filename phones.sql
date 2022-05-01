-- Table: public.phones

-- DROP TABLE IF EXISTS public.phones;

CREATE TABLE IF NOT EXISTS public.phones
(
    id bigint NOT NULL,
    phone text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT phones_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.phones
    OWNER to postgres;