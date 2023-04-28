-- Table: public.demo

-- DROP TABLE IF EXISTS public.demo;

CREATE TABLE IF NOT EXISTS public.demo
(
    id integer NOT NULL DEFAULT nextval('demo_id_seq'::regclass),
    keys jsonb,
    CONSTRAINT demo_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;


