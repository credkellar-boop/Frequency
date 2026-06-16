# ==========================================
# Stage 1: Build Binary
# ==========================================
FROM golang:1.23-alpine AS builder

RUN apk add --no-cache git build-base ca-certificates

WORKDIR /app

# 1. Copy all your repository files first to avoid the missing file error
COPY . .

# 2. If go.mod doesn't exist, automatically initialize and tidy it right here
RUN if [ ! -f go.mod ]; then \
        go mod init credkellar/frequency && \
        go mod tidy; \
    else \
        go mod tidy; \
    fi

# 3. Build the static binary
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o frequency .

# ==========================================
# Stage 2: Minimal Runtime
# ==========================================
FROM alpine:3.19 AS runner

RUN apk add --no-cache ca-certificates tzdata

WORKDIR /app

# Copy the compiled binary over
COPY --from=builder /app/frequency .

ENTRYPOINT ["./frequency"]

FROM golang:1.23-alpine AS builder
RUN apk add --no-cache git build-base ca-certificates
WORKDIR /app
COPY . .
RUN if [ ! -f go.mod ]; then \
        go mod init credkellar/frequency && \
        go mod tidy; \
    else \
        go mod tidy; \
    fi
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o frequency .

FROM alpine:3.19 AS runner
RUN apk add --no-cache ca-certificates tzdata
WORKDIR /app
COPY --from=builder /app/frequency .
ENTRYPOINT ["./frequency"]
