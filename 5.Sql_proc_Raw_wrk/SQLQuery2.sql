USE WeddingProjectDB
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Sangamithra Panneer selvam
-- Create date: 10-09-2022
-- Description:	RAW -> WRK
-- MOD DATE :
-- =============================================
CREATE PROC [BLD_WRK_WeddingProject]
AS
BEGIN
	-- This is my first proc
SELECT * FROM [dbo].[RAW_WeddingProject_10092022]
END
GO
