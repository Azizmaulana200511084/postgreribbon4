-- ----------------------------
-- Table structure for mahasiswa
-- ----------------------------
DROP TABLE IF EXISTS "public"."mahasiswa";
CREATE TABLE "public"."mahasiswa" (
  "id" serial primary key NOT NULL,
  "nim" varchar(10) COLLATE "pg_catalog"."default" NOT NULL,
  "nama" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "jk" char(1) COLLATE "pg_catalog"."default" NOT NULL,
  "kode_prodi" varchar(10) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of mahasiswa
-- ----------------------------
INSERT INTO "public"."mahasiswa" VALUES (2, '2222', 'Fina Wijaya', 'P', 'IND');
INSERT INTO "public"."mahasiswa" VALUES (3, '1111', 'Ahmad Bajuri', 'L', 'TIF');
