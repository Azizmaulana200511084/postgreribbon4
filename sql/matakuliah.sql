-- ----------------------------
-- Table structure for matakuliah
-- ----------------------------
DROP TABLE IF EXISTS "public"."matakuliah";
CREATE TABLE "public"."matakuliah" (
  "idmk" serial primary key NOT NULL,
  "kodemk" varchar(10) COLLATE "pg_catalog"."default" NOT NULL,
  "namamk" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "sks" integer NOT NULL
)
;

-- ----------------------------
-- Records of matakuliah
-- ----------------------------
INSERT INTO "public"."matakuliah" VALUES (1, '1001', 'Algoritma', 3);
INSERT INTO "public"."matakuliah" VALUES (2, '1002', 'Basis Data', 3);
INSERT INTO "public"."matakuliah" VALUES (3, '1003', 'Agama Islam', 2);
INSERT INTO "public"."matakuliah" VALUES (5, '1004', 'Java 2', 3);
