-- Table: public.followers

-- DROP TABLE IF EXISTS public.followers;

CREATE TABLE IF NOT EXISTS public.followers
(
    id bigint NOT NULL,
    username text COLLATE pg_catalog."default" NOT NULL,
    fullname text COLLATE pg_catalog."default",
    user_id bigint NOT NULL,
    CONSTRAINT followers_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.followers
    OWNER to postgres;