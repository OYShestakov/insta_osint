-- Table: public.emails

-- DROP TABLE IF EXISTS public.emails;

CREATE TABLE IF NOT EXISTS public.emails
(
    id bigint NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT emails_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.emails
    OWNER to postgres;