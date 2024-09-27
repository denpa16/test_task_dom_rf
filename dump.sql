--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--





--
-- Drop roles
--

DROP ROLE postgres;


--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:1ACyJ2l/2eczy/ELNJDJ0Q==$S1pyViTliOza4YPy8pJDYlvt/oE6YbtMfAVQ6OBKEyI=:Mr8k73Lv5QPIagKrLLPNvkBfHkZ7pDtg9gxTsptYN4I=';

--
-- User Configurations
--








--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO postgres;

\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: postgres
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: postgres
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS '';


--
-- Name: tasktype; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.tasktype AS ENUM (
    'PHONE',
    'EMAIL',
    'GPT'
);


ALTER TYPE public.tasktype OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: integration_service; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.integration_service (
    id integer NOT NULL,
    data json NOT NULL,
    task_type public.tasktype NOT NULL
);


ALTER TABLE public.integration_service OWNER TO postgres;

--
-- Name: integration_service_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.integration_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.integration_service_id_seq OWNER TO postgres;

--
-- Name: integration_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.integration_service_id_seq OWNED BY public.integration_service.id;


--
-- Name: integration_service id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.integration_service ALTER COLUMN id SET DEFAULT nextval('public.integration_service_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
93d05b467c90
\.


--
-- Data for Name: integration_service; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.integration_service (id, data, task_type) FROM stdin;
1	[{"source": "\\u0440\\u0430\\u0431 846)231.60.14 *139", "type": "\\u0421\\u0442\\u0430\\u0446\\u0438\\u043e\\u043d\\u0430\\u0440\\u043d\\u044b\\u0439", "phone": "+7 846 231-60-14 \\u0434\\u043e\\u0431. 139", "country_code": "7", "city_code": "846", "number": "2316014", "extension": "139", "provider": "\\u041e\\u041e\\u041e \\"\\u0421\\u0418\\u041f\\u0410\\u0423\\u0422\\u041d\\u042d\\u0422\\"", "country": "\\u0420\\u043e\\u0441\\u0441\\u0438\\u044f", "region": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0441\\u043a\\u0430\\u044f \\u043e\\u0431\\u043b\\u0430\\u0441\\u0442\\u044c", "city": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0430", "timezone": "UTC+4", "qc_conflict": 0, "qc": 0}]	PHONE
2	[{"source": "\\u0440\\u0430\\u0431 846)231.60.14 *139", "type": "\\u0421\\u0442\\u0430\\u0446\\u0438\\u043e\\u043d\\u0430\\u0440\\u043d\\u044b\\u0439", "phone": "+7 846 231-60-14 \\u0434\\u043e\\u0431. 139", "country_code": "7", "city_code": "846", "number": "2316014", "extension": "139", "provider": "\\u041e\\u041e\\u041e \\"\\u0421\\u0418\\u041f\\u0410\\u0423\\u0422\\u041d\\u042d\\u0422\\"", "country": "\\u0420\\u043e\\u0441\\u0441\\u0438\\u044f", "region": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0441\\u043a\\u0430\\u044f \\u043e\\u0431\\u043b\\u0430\\u0441\\u0442\\u044c", "city": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0430", "timezone": "UTC+4", "qc_conflict": 0, "qc": 0}]	PHONE
3	[{"source": "\\u0440\\u0430\\u0431 846)231.60.14 *139", "type": "\\u0421\\u0442\\u0430\\u0446\\u0438\\u043e\\u043d\\u0430\\u0440\\u043d\\u044b\\u0439", "phone": "+7 846 231-60-14 \\u0434\\u043e\\u0431. 139", "country_code": "7", "city_code": "846", "number": "2316014", "extension": "139", "provider": "\\u041e\\u041e\\u041e \\"\\u0421\\u0418\\u041f\\u0410\\u0423\\u0422\\u041d\\u042d\\u0422\\"", "country": "\\u0420\\u043e\\u0441\\u0441\\u0438\\u044f", "region": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0441\\u043a\\u0430\\u044f \\u043e\\u0431\\u043b\\u0430\\u0441\\u0442\\u044c", "city": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0430", "timezone": "UTC+4", "qc_conflict": 0, "qc": 0}]	PHONE
4	[{"source": "\\u0440\\u0430\\u0431 846)231.60.14 *139", "type": "\\u0421\\u0442\\u0430\\u0446\\u0438\\u043e\\u043d\\u0430\\u0440\\u043d\\u044b\\u0439", "phone": "+7 846 231-60-14 \\u0434\\u043e\\u0431. 139", "country_code": "7", "city_code": "846", "number": "2316014", "extension": "139", "provider": "\\u041e\\u041e\\u041e \\"\\u0421\\u0418\\u041f\\u0410\\u0423\\u0422\\u041d\\u042d\\u0422\\"", "country": "\\u0420\\u043e\\u0441\\u0441\\u0438\\u044f", "region": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0441\\u043a\\u0430\\u044f \\u043e\\u0431\\u043b\\u0430\\u0441\\u0442\\u044c", "city": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0430", "timezone": "UTC+4", "qc_conflict": 0, "qc": 0}]	EMAIL
5	[{"source": "\\u0440\\u0430\\u0431 846)231.60.14 *139", "type": "\\u0421\\u0442\\u0430\\u0446\\u0438\\u043e\\u043d\\u0430\\u0440\\u043d\\u044b\\u0439", "phone": "+7 846 231-60-14 \\u0434\\u043e\\u0431. 139", "country_code": "7", "city_code": "846", "number": "2316014", "extension": "139", "provider": "\\u041e\\u041e\\u041e \\"\\u0421\\u0418\\u041f\\u0410\\u0423\\u0422\\u041d\\u042d\\u0422\\"", "country": "\\u0420\\u043e\\u0441\\u0441\\u0438\\u044f", "region": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0441\\u043a\\u0430\\u044f \\u043e\\u0431\\u043b\\u0430\\u0441\\u0442\\u044c", "city": "\\u0421\\u0430\\u043c\\u0430\\u0440\\u0430", "timezone": "UTC+4", "qc_conflict": 0, "qc": 0}]	EMAIL
6	{"result": {"alternatives": [{"message": {"role": "assistant", "text": "\\u041e\\u0448\\u0438\\u0431\\u043a\\u0438 \\u0441\\u0430\\u043c\\u0438 \\u0441\\u0435\\u0431\\u044f \\u043d\\u0435 \\u0438\\u0441\\u043f\\u0440\\u0430\\u0432\\u044f\\u0442."}, "status": "ALTERNATIVE_STATUS_FINAL"}], "usage": {"inputTextTokens": "29", "completionTokens": "9", "totalTokens": "38"}, "modelVersion": "07.03.2024"}}	GPT
7	{"result": {"alternatives": [{"message": {"role": "assistant", "text": "\\u041e\\u0448\\u0438\\u0431\\u043a\\u0438 \\u0441\\u0430\\u043c\\u0438 \\u0441\\u0435\\u0431\\u044f \\u043d\\u0435 \\u0438\\u0441\\u043f\\u0440\\u0430\\u0432\\u044f\\u0442."}, "status": "ALTERNATIVE_STATUS_FINAL"}], "usage": {"inputTextTokens": "29", "completionTokens": "9", "totalTokens": "38"}, "modelVersion": "07.03.2024"}}	GPT
\.


--
-- Name: integration_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.integration_service_id_seq', 7, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: integration_service integration_service_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.integration_service
    ADD CONSTRAINT integration_service_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

