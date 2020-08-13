/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : localhost:3306
 Source Schema         : pvs

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 13/08/2020 16:15:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for pvs_tasks
-- ----------------------------
DROP TABLE IF EXISTS `pvs_tasks`;
CREATE TABLE `pvs_tasks` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `status` int(11) DEFAULT '1' COMMENT '任务状态, 1:新建, 2: 运行中, 3:完成,4:停止,5 删除',
  `create_time` datetime NOT NULL COMMENT '任务创建时间',
  `task_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '任务 id',
  `end_time` datetime DEFAULT NULL COMMENT '任务结束时间',
  `vul_no` int(11) DEFAULT '0' COMMENT '发现的漏洞数量',
  `creator` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '任务创建者',
  `targets` text COMMENT '任务目标',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for pvs_invoker
-- ----------------------------
DROP TABLE IF EXISTS `pvs_invoker`;
CREATE TABLE `pvs_invoker` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `app_id` varchar(100) DEFAULT NULL,
  `secret_key` varchar(100) DEFAULT NULL,
  `active` smallint(2) DEFAULT NULL,
  `nick_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
